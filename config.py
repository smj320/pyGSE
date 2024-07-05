def get_dbconfig():
    return {
        "user": "root",
        "password": "pass",
        "host": "localhost",
        "port": 3306,
        "database": "df3_gse"
    }


def get_element():
    return {
        "FS": [0, 4],
        "TI": [4, 4],
        "STAT": [8, 1],
        "PDU_V": [9, 1],
        "DMY1": [10, 1],
        "BAT_V": [11, 1],
        "BAT_T": [12, 1],
        "SYS_T": [13, 1],
        "SYS_H": [14, 1],
        "SYS_P": [15, 1],
        "GND_P": [16, 2],
        "MOT_V": [18, 1],
        "DMY2": [19, 1],
        "MOT_T": [20, 1],
        "GEA_T": [21, 1],
        "MOT_R": [22, 1],
        "DMY3": [23, 1],
        "LIQ1_T": [24, 2],
        "LIQ1_P": [26, 2],
        "LIQ2_T": [28, 2],
        "BOA1_D": [30, 2],
        "GRA_X": [32, 2],
        "GRA_Y": [34, 2],
        "GRA_Z": [36, 2],
        "ACC_X": [38, 2],
        "ACC_Y": [40, 2],
        "ACC_Z": [42, 2],
        "ROT_X": [44, 2],
        "ROT_Y": [46, 2],
        "ROT_Z": [48, 2],
        "MAG_X": [50, 2],
        "MAG_Y": [52, 2],
        "MAG_Z": [54, 2],
        "BOA2_D": [56, 2],
        "LIQ3_T": [58, 2],
        "LIQ4_T": [60, 2],
        "CSUM": [79, 1]
    }


def get_fmt():
    ll = [4, 28, 53]
    return {  # a,b,x,y,fmt
        "FS": [1.0, 0.0, 4, ll[0], "FS        %08X"],
        "TI": [1.0, 0.0, 5, ll[0], "TI        %08d"],
        "STAT": [1.0, 0.0, 6, ll[0], "STAT      %08d"],
        #
        "PDU_V": [1.0, 0.0, 8, ll[0], "PDU_V  %7.2f [V]"],
        "DMY1": [1.0, 0.0, 9, ll[0], "DMY1        %02d [dec]"],
        "BAT_V": [1.0, 0.0, 10, ll[0], "BAT_V  %7.2f [V]"],
        "BAT_T": [0.8, 0.6, 11, ll[0], "BAT_T  %7.2f [C]"],
        # x*1
        "SYS_T": [1.0, 0.0, 13, ll[0], "SYS_T  %7.2f [C]"],
        "SYS_H": [1.0, 0.0, 14, ll[0], "SYS_H  %7.2f [%%]"],
        "SYS_P": [1.0, 0.0, 15, ll[0], "SYS_P  %7.2f [atm]"],
        #
        "GND_P": [1.0, 0.0, 4, ll[1], "GND_P   %7.2f [atm]"],
        "MOT_V": [1.0, 0.0, 5, ll[1], "MOT_V   %7.2f [V]"],
        "DMY2": [1.0, 0.0, 6, ll[1], "DMY2         %02d [dec]"],
        "MOT_T": [0.8, 0.6, 7, ll[1], "MOT_T   %7.2f [C]"],
        "GEA_T": [0.8, 0.6, 8, ll[1], "GEA_T   %7.2f [C]"],
        "MOT_R": [1.0, 0.0, 9, ll[1], "MOT_R   %7.2f [rpm]"],
        "DMY3": [1.0, 0.0, 10, ll[1], "DMY3         %02d [dec]"],
        #
        "LIQ1_T": [0.8, 0.6, 12, ll[1], "LIQ1_T  %7.2f [C]"],
        "LIQ1_P": [1.0, 0.0, 13, ll[1], "LIQ1_P  %7.2f [atm]"],
        "LIQ2_T": [0.8, 0.6, 14, ll[1], "LIQ2_T  %7.2f [C]"],
        "BOA1_D": [1.0, 0, 15, ll[1], "BOA1_D  %7.2f [mm]"],
        # x/100
        "GRA_X": [0.01, 0, 4, ll[2], "GRA_X   %7.2f [m/s^2]"],
        "GRA_Y": [0.01, 0, 5, ll[2], "GRA_Y   %7.2f [m/s^2]"],
        "GRA_Z": [0.01, 0, 6, ll[2], "GRA_Z   %7.2f [m/s^2]"],
        # x/100
        "ACC_X": [0.01, 0, 8, ll[2], "ACC_X   %7.2f [m/s^2]"],
        "ACC_Y": [0.01, 0, 9, ll[2], "ACC_Y   %7.2f [m/s^2]"],
        "ACC_Z": [0.01, 0, 10, ll[2], "ACC_Z   %7.2f [m/s^2]"],
        # x/100
        "ROT_X": [0.01, 0, 12, ll[2], "ROT_X   %7.2f [rad/s]"],
        "ROT_Y": [0.01, 0, 13, ll[2], "ROT_Y   %7.2f [rad/s]"],
        "ROT_Z": [0.01, 0, 14, ll[2], "ROT_Z   %7.2f [rad/s]"],
        # x/24.0
        "MAG_X": [0.0417, 0, 16, ll[2], "MAG_X   %7.2f [mT]"],
        "MAG_Y": [0.0417, 0, 17, ll[2], "MAG_Y   %7.2f [mT]"],
        "MAG_Z": [0.0417, 0, 18, ll[2], "MAG_Z   %7.2f [mT]"],
        # 検層機用
        "BOA2_D": [1.0, 0, 16, ll[1], "BOA2_D  %7.2f [mT]"],
        "LIQ3_T": [1.0, 0, 17, ll[1], "LIQ3_T  %7.2f [mT]"],
        "LIQ4_T": [1.0, 0, 18, ll[1], "LIQ4_T  %7.2f [mT]"],
        # Check sum
        "CSUM": [1.0, 0.0, 20, ll[0], "CSUM        %02X [hex]"]
    }
