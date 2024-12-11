"""
df3_gseのrecordテーブルから、データをプロットする
"""
# モジュールの取得
# 基本
import math
import datetime as dt
# DB
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
# プロット
import matplotlib
from matplotlib import dates
from matplotlib import pyplot as plt
# Curses
import curses
# Config
import config


def get_time_range():
    """ 時刻範囲とデータ取得用SQLを生成 """
    # ティック刻み15分の場合
    t0 = dt.datetime.now()
    u_stop = (math.floor(t0.timestamp() / (15 * 60)) + 1) * 15 * 60
    start = dt.datetime.fromtimestamp(u_stop - 2 * 60 * 60)
    stop = dt.datetime.fromtimestamp(u_stop)
    start_str = start.strftime('%Y-%m-%d %H:%M:%S')

    # データ取得用SQL
    cmd = "select * from record where TS > '%s'" % start_str
    return t0, start, stop, cmd


def update(engine, fig, axs, d_cfg):
    """ 描画の更新 """
    # 時間軸の設定
    t0, start, stop, query = get_time_range()
    for num in range(6):
        axs[num].set_xlim(start, stop)

    # DB接続と解除
    sqlcmd = f'select * from record where TS > \'{start.strftime("%Y-%m-%d %H:%M:%S")}\''
    df = pd.DataFrame(engine.connect().execute(text(sqlcmd)))
    fig.suptitle("Drill Monitor [%s]" % t0.strftime("%F %H:%M:%S"))

    # プロット準備

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    labels_a = [
        ['BAT_T', 'SYS_T', 'SYS_H', 'MOT_T', 'GEA_T', 'LIQ1_T', 'LIQ2_T'],
        ['PDU_V', 'BAT_V', 'MOT_V'],
        ['MOT_R', 'GND_P'],
        ['GRA_X', 'GRA_Y', 'GRA_Z'],
        ['ROT_X', 'ROT_Y', 'ROT_Z'],
        ['MAG_X', 'MAG_Y', 'MAG_Z']
    ]

    # プロット1 温度
    lines = []  # 消去用
    np = 0
    for labels in labels_a:
        nc = 0
        for lb in labels:
            [a, b] = [d_cfg[lb][0], d_cfg[lb][1]]
            # BAT_Vだけ10倍に拡大
            val = (df[lb] * a + b) * 10 if lb == 'BAT_V' else df[lb] * a + b
            lbs = "BAT_V*10" if lb == 'BAT_V' else lb
            # 表示
            lines.append(axs[np].plot(df['TS'], val, ".", label=lbs, color=colors[nc]), )
            nc += 1
        axs[np].legend(loc='lower left')
        np += 1

    # プロット2 電力
    # 後始末
    plt.pause(1)
    for ll in lines:
        ll[0].remove()


def main(stdscr):
    # DB接続と解除
    d_cfg = config.get_fmt()
    dbc = config.get_dbconfig()
    url = f'mysql+pymysql://%s:%s@%s:%d/%s' % (dbc['user'], dbc['password'], dbc['host'], dbc['port'], dbc['database'])
    engine = create_engine(url, echo=False)

    # 画面準備
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.addstr(1, 1, " DRILL MONITOR Graph running... (Exit: ESC key)")

    # キャンバスの準備
    # macはデフォルトの/usr/bin/python3でないと色々失敗する。
    matplotlib.use("TkAgg")

    matplotlib.rcParams['font.family'] = ['IPAexGothic']
    fig, axs_a = plt.subplots(3, 2, figsize=(14, 8))
    plt.subplots_adjust(hspace=0.5)
    axs = []
    for col in range(2):
        for row in range(3):
            axs.append(axs_a[row, col])

    # 座標軸の設定
    params = [  # Title, Yラベル, Y範囲
        ["Temperature", "Temperature (C)", [-60, 60]],
        ["Power Supply", "Power Supply (V)", [0, 240]],
        ["Drill Status", "Ground Pressure (kgw)\nMotor Speed (rpm)", [-50, 50]],
        ["Gravity", "Gravity (u/s^2)", [-20, 20]],
        ["ROT", "Angular speed (deg/s)", [-60, 60]],
        ["GEO MAG", "Geo MAG (mT)", [-200, 200]],
    ]
    for i in range(len(params)):
        axs[i].set_title(params[i][0])
        axs[i].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
        axs[i].set_ylabel(params[i][1])
        axs[i].set_ylim(params[i][2])
        axs[i].grid()

    # データ描画
    while True:
        update(engine, fig, axs, d_cfg)
        rtc = stdscr.getch()
        if rtc == 0x1b:  # ESC
            break

    # 画面の後始末
    curses.nocbreak()
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    curses.wrapper(main)
