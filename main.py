import config
import curses
from curses import wrapper
import serial
from serial.tools import list_ports


def decode(elements, fifo):
    """ config.pyのelementに基づいて、FIFOの内容をデコードする """
    values = {}
    for e in elements:
        datum = fifo[e['pos']:e['pos'] + e['len']]
        if e['len'] == 4:
            if e['label'] == "FS":
                vv = int.from_bytes(datum, byteorder='big')
            else:  # TI
                vv = int.from_bytes(datum, byteorder='little')
        else:  # 2byteでも1byteでも符号付き
            if e['label'] == "CSUM":
                vv = int.from_bytes(datum, byteorder='little')
            else:
                vv = int.from_bytes(datum, byteorder='little', signed=True)
        values[e['label']] = vv

    return values


def display_data(stdscr, values, fmt):
    """ decodeで分解したfifoの内容を表示する """
    for f in fmt:
        v = values[f['label']] * f['a'] + f['b']
        stdscr.addstr(f['x'], f['y'], f['fmt'] % v)


def get_usb_ports():
    """ Serialポートを探索して、usbserialを含むポートをリストで返す """
    ports = list(list_ports.comports())
    usb_ports = []
    for port in ports:
        name = port.device
        if name.startswith('/dev/cu.usb'):  # usbmodemとusbserialがある。
            usb_ports.append(port.device)
    return usb_ports


def main(stdscr):
    # config.pyからテレメのビット位置、表示場所のデータを取得
    elm = config.get_element()
    fmt = config.get_fmt()

    # USBポートを取得
    usb_ports = get_usb_ports()
    if len(usb_ports) != 1:
        print("Non single USB serial")
        exit(-1)

    # 受診バッファとポート準備
    fifo = bytearray(80)
    reader = serial.Serial(usb_ports[0], 1200, timeout=3)

    # 画面準備
    curses.noecho()
    curses.cbreak()
    stdscr = curses.initscr()
    stdscr.keypad(True)
    stdscr.nodelay(True)

    # 受信開始
    while True:
        c = reader.read()
        # FIFOにデータを詰める
        fifo.append(int.from_bytes(c))
        fifo.pop(0)
        # 先頭がフレームシンクに一致していれば同期完了
        if [fifo[0], fifo[1], fifo[2], fifo[3]] == [0xeb, 0x90, 0x38, 0xC7]:
            # タイトル
            stdscr.addstr(2, 4, "DRILL MONITOR (Exit: ESC key)")
            # データ
            values = decode(elm, fifo)
            display_data(stdscr, values, fmt)
            # 更新
            stdscr.refresh()
            rtc = stdscr.getch()
            if rtc == 0x1b:     # ESC
                break

    # 終了処理
    curses.nocbreak()
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
