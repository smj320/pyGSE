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
    # 描画パラメータ取得
    t0, start, stop, query = get_time_range()
    axs[0, 0].set_xlim(start, stop)
    axs[1, 0].set_xlim(start, stop)
    axs[2, 0].set_xlim(start, stop)
    axs[0, 1].set_xlim(start, stop)
    axs[1, 1].set_xlim(start, stop)
    axs[2, 1].set_xlim(start, stop)

    # DB接続と解除
    sqlcmd = "select * from record where TS > '%s'" % start.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.read_sql(sqlcmd, con=engine)
    fig.suptitle("Drill Monitor [%s]" % t0.strftime("%F %H:%M:%S"))

    lines = []
    # プロット1 温度
    line = [
        axs[0, 0].plot(df.TS, df.BAT_T * d_cfg["BAT_T"][0] + d_cfg["BAT_T"][1], ".", label="BAT_T", color='g'),
        axs[0, 0].plot(df.TS, df.SYS_T * d_cfg["SYS_T"][0] + d_cfg["SYS_T"][1], ".", label="SYS_T", color='r'),
        axs[0, 0].plot(df.TS, df.SYS_H * d_cfg["SYS_H"][0] + d_cfg["SYS_H"][1], ".", label="SYS_H", color='b'),
        axs[0, 0].plot(df.TS, df.MOT_T * d_cfg["MOT_T"][0] + d_cfg["MOT_T"][1], ".", label="MOT_T", color='y'),
        axs[0, 0].plot(df.TS, df.GEA_T * d_cfg["GEA_T"][0] + d_cfg["GEA_T"][1], ".", label="GEA_T", color='m'),
        axs[0, 0].plot(df.TS, df.LIQ1_T * d_cfg["LIQ1_T"][0] + d_cfg["LIQ1_T"][1], ".", label="LIQ1_T", color='m'),
        axs[0, 0].plot(df.TS, df.LIQ2_T * d_cfg["LIQ2_T"][0] + d_cfg["LIQ2_T"][1], ".", label="LIQ2_T", color='m')
    ]
    axs[0, 0].legend(loc='lower left')
    lines.append(line)

    # プロット2 電力
    line = [
        axs[1, 0].plot(df.TS, df.PDU_V * d_cfg["PDU_V"][0] + d_cfg["PDU_V"][1], ".", label="PDU_V", color='g'),
        axs[1, 0].plot(df.TS, df.BAT_V * d_cfg["BAT_V"][0] + d_cfg["BAT_V"][1], ".", label="BAT_V", color='r'),
        axs[1, 0].plot(df.TS, df.MOT_V * d_cfg["MOT_V"][0] + d_cfg["MOT_V"][1], ".", label="MOT_V", color='b')
    ]
    axs[1, 0].legend(loc='lower left')
    lines.append(line)

    # プロット3 掘削ステータス
    line = [
        axs[2, 0].plot(df.TS, df.MOT_R * d_cfg["MOT_R"][0] + d_cfg["MOT_R"][1], ".", label="MOT_R", color='g'),
        axs[2, 0].plot(df.TS, df.GND_P * d_cfg["GND_P"][0] + d_cfg["GND_P"][1], ".", label="GND_P", color='r'),
    ]
    axs[2, 0].legend(loc='lower left')
    lines.append(line)

    # プロット4 重力
    line = [
        axs[0, 1].plot(df.TS, df.GRA_X * d_cfg["GRA_X"][0] + d_cfg["GRA_X"][1], ".", label="GRA_X", color='g'),
        axs[0, 1].plot(df.TS, df.GRA_Y * d_cfg["GRA_Y"][0] + d_cfg["GRA_Y"][1], ".", label="GRA_Y", color='r'),
        axs[0, 1].plot(df.TS, df.GRA_Z * d_cfg["GRA_Z"][0] + d_cfg["GRA_Z"][1],".", label="GRA_Z", color='b')
    ]
    axs[0, 1].legend(loc='lower left')
    lines.append(line)

    # プロット4 角速度
    line = [
        axs[1, 1].plot(df.TS, df.ROT_X * d_cfg["ROT_X"][0] + d_cfg["ROT_X"][1], ".", label="ROT_X", color='g'),
        axs[1, 1].plot(df.TS, df.ROT_Y * d_cfg["ROT_Y"][0] + d_cfg["ROT_Y"][1], ".", label="ROT_Y", color='r'),
        axs[1, 1].plot(df.TS, df.ROT_Z * d_cfg["ROT_Z"][0] + d_cfg["ROT_Z"][1], ".", label="ROT_Z", color='b')
    ]
    axs[1, 1].legend(loc='lower left')
    lines.append(line)

    # プロット4 地磁気
    line = [
        axs[2, 1].plot(df.TS, df.MAG_X * d_cfg["MAG_X"][0] + d_cfg["MAG_X"][1], ".", label="MAG_X", color='g'),
        axs[2, 1].plot(df.TS, df.MAG_Y * d_cfg["MAG_Y"][0] + d_cfg["MAG_Y"][1], ".", label="MAG_Y", color='r'),
        axs[2, 1].plot(df.TS, df.MAG_Z * d_cfg["MAG_Z"][0] + d_cfg["MAG_Z"][1], ".", label="MAG_Z", color='b')
    ]
    axs[2, 1].legend(loc='lower left')
    lines.append(line)

    # 後始末
    plt.pause(1)
    for lls in lines:
        for ll in lls:
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
    stdscr.addstr(1, 1, "GSE Graphic running... [stop ESC]")

    # キャンバスの準備
    matplotlib.use("TkAgg")
    matplotlib.rcParams['font.family'] = ['IPAexGothic']
    fig, axs = plt.subplots(3, 2, figsize=(14, 8))
    plt.subplots_adjust(hspace=0.5)

    # 座標軸の設定
    axs[0, 0].set_title("Temperature")
    axs[0, 0].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[0, 0].set_ylabel("Temperature (C)")
    axs[0, 0].set_ylim(-60, 60)
    axs[0, 0].grid()
    axs[1, 0].set_title("Power Supply")
    axs[1, 0].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[1, 0].set_ylabel("Power Supply (V)")
    axs[1, 0].set_ylim(0, 240)
    axs[1, 0].grid()
    axs[2, 0].set_title("Drill Status")
    axs[2, 0].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[2, 0].set_ylabel("Ground Pressure (kgw)")
    axs[2, 0].set_ylim(-50, 50)
    axs[2, 0].grid()
    axs[0, 1].set_title("Gravity")
    axs[0, 1].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[0, 1].set_ylabel("Gravity (m/s^2)")
    axs[0, 1].set_ylim(-20, 20)
    axs[0, 1].grid()
    axs[1, 1].set_title("ROT")
    axs[1, 1].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[1, 1].set_ylabel("Angular speed (deg/s)")
    axs[1, 1].set_ylim(-100, 100)
    axs[1, 1].grid()
    axs[2, 1].set_title("GEO MAG")
    axs[2, 1].xaxis.set_major_formatter(dates.DateFormatter('%m/%d\n%H:%M'))
    axs[2, 1].set_ylabel("Geo MAG (mT)")
    axs[2, 1].set_ylim(-200, 200)
    axs[2, 1].grid()

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
