# import curses
import re
import struct
import serial
from serial.tools import list_ports
# import numpy as np

BYTEARRAY_INPUT = bytearray([0xeb, 0x90, 0x79, 0xE9, 0x34, 0x12])
USB_PORT_REGEX = "/dev/cu\.usbmodem"

# Label, start, len, x, y
global Elm
Ele = [
    ["FS", 0, 4],
    ["TI", 4, 4],
    ["STAT", 8, 1],
    ["PDU_V", 9, 1],
    ["DMY1", 10, 1],
    ["BAT_V", 11, 1],
    ["BAT_T", 12, 1],
    ["SYS_T", 13, 1],
    ["SYS_H", 14, 1],
    ["SYS_P", 15, 1],
    ["GND_P", 16, 2],
    ["MOT_V", 18, 1],
    ["MOT_A", 19, 1],
    ["MOT_T", 20, 1],
    ["GEA_T", 21, 1],
    ["MOT_R", 22, 1],
    ["DMY3", 23, 1],
    ["LIQ1_T", 24, 2],
    ["LIQ1_P", 26, 2],
    ["LIQ2_T", 28, 2],
    ["BOA_D", 30, 2],
    ["GRA_X", 32, 2],
    ["GRA_Y", 34, 2],
    ["GRA_Z", 36, 2],
    ["ACC_X", 38, 2],
    ["ACC_Y", 40, 2],
    ["ACC_Z", 42, 2],
    ["ROT_X", 44, 2],
    ["ROT_Y", 46, 2],
    ["ROT_Z", 48, 2],
    ["MAX_X", 50, 2],
    ["MAX_Y", 52, 2],
    ["MAX_Z", 54, 2],
]


def get_usb_ports():
    ports = list(list_ports.comports())
    usb_ports = [port.device for port in ports if re.match(USB_PORT_REGEX, port.device)]
    return usb_ports


def convert_bytes_to_int():
    file_size = int.from_bytes(BYTEARRAY_INPUT[0:3], byteorder='big')
    time_interval = int.from_bytes(BYTEARRAY_INPUT[4:5], byteorder='little')
    print(file_size)


def check_multiple_usb_ports(usb_ports):
    if len(usb_ports) != 1:
        print("Multiple USB ports")
        exit(-1)
    print(usb_ports[0])


def decode(fl2):
    global Elm

    for elm in Elm:
        datum = fl2[elm[0]:elm[0] + elm[1]]
        value = struct.unpack('!f', bytes.fromhex(datum))[0]


def main():
    convert_bytes_to_int()
    usb_ports = get_usb_ports()
    check_multiple_usb_ports(usb_ports)

    f = open("test.log", "w")
    fl = bytearray(80)
    reader = serial.Serial('/dev/cu.usbmodem1443302', 1200, timeout=3)

    for i in range(1000):
        c = reader.read()
        fl.pop(0)
        fl.append(int.from_bytes(c))
        if [fl[0], fl[1], fl[2], fl[3]] == [0xeb, 0x90, 0x38, 0xC7]:
            fl2 = fl
            decode(fl2)

    f.close()
    # std_scr = curses.initscr()
    # std_scr.addstr(1, 10, "Pretty text")
    # std_scr.refresh()
    # curses.endwin()


if __name__ == '__main__':
    main()
