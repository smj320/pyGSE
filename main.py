import tlm_config
import curses
import re
import serial
from serial.tools import list_ports

# import numpy as np

FSW = [0xeb, 0x90, 0x38, 0xC7]


def decode(elm, fl):
    values = {}
    for e in elm:
        datum = fl[e['pos']:e['pos'] +e['len']]
        if e['len']== 4:
            if e['label']== "FS":
                vv = int.from_bytes(datum, byteorder='little')
            else:  # TI
                vv = int.from_bytes(datum, byteorder='big')
        else:
            vv = int.from_bytes(datum, byteorder='big')
        values[e['label']] = vv

    return values


def put_data(values):
    for v in values:
        print(v)


def get_usb_ports():
    ports = list(list_ports.comports())
    usb_ports = []
    for port in ports:
        if re.match(r'/dev/cu\.usbmodem', port.device):
            usb_ports.append(port.device)
    return usb_ports


def main():
    elm = tlm_config.get_element()

    usb_ports = get_usb_ports()
    if len(usb_ports) != 1:
        print("Non single USB serial")
        exit(-1)

    f = open("test.log", "w")
    fl = bytearray(80)
    reader = serial.Serial(usb_ports[0], 1200, timeout=3)

    for i in range(1000):
        c = reader.read()
        fl.pop(0)
        fl.append(int.from_bytes(c))
        if [fl[0], fl[1], fl[2], fl[3]] == FSW:
            values = decode(elm, fl)
            put_data(values)

    # curses.endwin()
    f.close()


if __name__ == '__main__':
    main()
