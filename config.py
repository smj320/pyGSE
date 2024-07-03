def get_dbconfig():
    return {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "pass",
        "database": "df3_gse"
    }


def get_element():
    return [
        {"label": "FS", "pos": 0, "len": 4},
        {"label": "TI", "pos": 4, "len": 4},
        {"label": "STAT", "pos": 8, "len": 1},
        {"label": "PDU_V", "pos": 9, "len": 1},
        {"label": "DMY1", "pos": 10, "len": 1},
        {"label": "BAT_V", "pos": 11, "len": 1},
        {"label": "BAT_T", "pos": 12, "len": 1},
        {"label": "SYS_T", "pos": 13, "len": 1},
        {"label": "SYS_H", "pos": 14, "len": 1},
        {"label": "SYS_P", "pos": 15, "len": 1},
        {"label": "GND_P", "pos": 16, "len": 2},
        {"label": "MOT_V", "pos": 18, "len": 1},
        {"label": "DMY2", "pos": 19, "len": 1},
        {"label": "MOT_T", "pos": 20, "len": 1},
        {"label": "GEA_T", "pos": 21, "len": 1},
        {"label": "MOT_R", "pos": 22, "len": 1},
        {"label": "DMY3", "pos": 23, "len": 1},
        {"label": "LIQ1_T", "pos": 24, "len": 2},
        {"label": "LIQ1_P", "pos": 26, "len": 2},
        {"label": "LIQ2_T", "pos": 28, "len": 2},
        {"label": "BOA_D", "pos": 30, "len": 2},
        {"label": "GRA_X", "pos": 32, "len": 2},
        {"label": "GRA_Y", "pos": 34, "len": 2},
        {"label": "GRA_Z", "pos": 36, "len": 2},
        {"label": "ACC_X", "pos": 38, "len": 2},
        {"label": "ACC_Y", "pos": 40, "len": 2},
        {"label": "ACC_Z", "pos": 42, "len": 2},
        {"label": "ROT_X", "pos": 44, "len": 2},
        {"label": "ROT_Y", "pos": 46, "len": 2},
        {"label": "ROT_Z", "pos": 48, "len": 2},
        {"label": "MAG_X", "pos": 50, "len": 2},
        {"label": "MAG_Y", "pos": 52, "len": 2},
        {"label": "MAG_Z", "pos": 54, "len": 2},
        {"label": "BOA2_D", "pos": 56, "len": 2},
        {"label": "LIQ3_T", "pos": 58, "len": 2},
        {"label": "LIQ4_T", "pos": 60, "len": 2},
        {"label": "CSUM", "pos": 79, "len": 1}
    ]


def get_fmt():
    ll = [4, 28, 53]
    return [
        {"label": "FS", "a": 1, "b": 0, "x": 4, "y": ll[0], "fmt": "FS        %08X"},
        {"label": "TI", "a": 1, "b": 0, "x": 5, "y": ll[0], "fmt": "TI        %08d"},
        {"label": "STAT", "a": 1, "b": 0, "x": 6, "y": ll[0], "fmt": "STAT      %08d"},
        #
        {"label": "PDU_V", "a": 1, "b": 0, "x": 8, "y": ll[0], "fmt": "PDU_V  %7.2f [V]"},
        {"label": "DMY1", "a": 1, "b": 0, "x": 9, "y": ll[0], "fmt": "DMY1        %02d [dec]"},
        {"label": "BAT_V", "a": 1, "b": 0, "x": 10, "y": ll[0], "fmt": "BAT_V  %7.2f [V]"},
        {"label": "BAT_T", "a": 0.8, "b": 0.6, "x": 11, "y": ll[0], "fmt": "BAT_T  %7.2f [C]"},
        # x*1
        {"label": "SYS_T", "a": 1, "b": 0, "x": 13, "y": ll[0], "fmt": "SYS_T  %7.2f [C]"},
        {"label": "SYS_H", "a": 1, "b": 0, "x": 14, "y": ll[0], "fmt": "SYS_H  %7.2f [%%]"},
        {"label": "SYS_P", "a": 1, "b": 0, "x": 15, "y": ll[0], "fmt": "SYS_P  %7.2f [atm]"},
        #
        {"label": "GND_P", "a": 1, "b": 0, "x": 4, "y": ll[1], "fmt": "GND_P   %7.2f [atm]"},
        {"label": "MOT_V", "a": 1, "b": 0, "x": 5, "y": ll[1], "fmt": "MOT_V   %7.2f [V]"},
        {"label": "DMY2", "a": 1, "b": 0, "x": 6, "y": ll[1], "fmt": "DMY2         %02d [dec]"},
        {"label": "MOT_T", "a": 0.8, "b": 0.6, "x": 7, "y": ll[1], "fmt": "MOT_T   %7.2f [C]"},
        {"label": "GEA_T", "a": 0.8, "b": 0.6, "x": 8, "y": ll[1], "fmt": "GEA_T   %7.2f [C]"},
        {"label": "MOT_R", "a": 1, "b": 0, "x": 9, "y": ll[1], "fmt": "MOT_R   %7.2f [rpm]"},
        {"label": "DMY3", "a": 1, "b": 0, "x": 10, "y": ll[1], "fmt": "DMY3         %02X [hex]"},
        #
        {"label": "LIQ1_T", "a": 0.8, "b": 0.6, "x": 12, "y": ll[1], "fmt": "LIQ1_T  %7.2f [C]"},
        {"label": "LIQ1_P", "a": 1, "b": 0, "x": 13, "y": ll[1], "fmt": "LIQ1_P  %7.2f [atm]"},
        {"label": "LIQ2_T", "a": 0.8, "b": 0.6, "x": 14, "y": ll[1], "fmt": "LIQ2_T  %7.2f [C]"},
        {"label": "BOA_D", "a": 1, "b": 0, "x": 15, "y": ll[1], "fmt": "BOA_D   %7.2f [mm]"},
        # x/100
        {"label": "GRA_X", "a": 0.01, "b": 0, "x": 4, "y": ll[2], "fmt": "GRA_X   %7.2f [m/s^2]"},
        {"label": "GRA_Y", "a": 0.01, "b": 0, "x": 5, "y": ll[2], "fmt": "GRA_Y   %7.2f [m/s^2]"},
        {"label": "GRA_Z", "a": 0.01, "b": 0, "x": 6, "y": ll[2], "fmt": "GRA_Z   %7.2f [m/s^2]"},
        # x/100
        {"label": "ACC_X", "a": 0.01, "b": 0, "x": 8, "y": ll[2], "fmt": "ACC_X   %7.2f [m/s^2]"},
        {"label": "ACC_Y", "a": 0.01, "b": 0, "x": 9, "y": ll[2], "fmt": "ACC_Y   %7.2f [m/s^2]"},
        {"label": "ACC_Z", "a": 0.01, "b": 0, "x": 10, "y": ll[2], "fmt": "ACC_Z   %7.2f [m/s^2]"},
        # x/100
        {"label": "ROT_X", "a": 0.01, "b": 0, "x": 12, "y": ll[2], "fmt": "ROT_X   %7.2f [rad/s]"},
        {"label": "ROT_Y", "a": 0.01, "b": 0, "x": 13, "y": ll[2], "fmt": "ROT_Y   %7.2f [rad/s]"},
        {"label": "ROT_Z", "a": 0.01, "b": 0, "x": 14, "y": ll[2], "fmt": "ROT_Z   %7.2f [rad/s]"},
        # x/24.0
        {"label": "MAG_X", "a": 0.0417, "b": 0, "x": 16, "y": ll[2], "fmt": "MAG_X   %7.2f [mT]"},
        {"label": "MAG_Y", "a": 0.0417, "b": 0, "x": 17, "y": ll[2], "fmt": "MAG_Y   %7.2f [mT]"},
        {"label": "MAG_Z", "a": 0.0417, "b": 0, "x": 18, "y": ll[2], "fmt": "MAG_Z   %7.2f [mT]"},
        # 検層機用
        {"label": "BOA2_D", "a": 1.0, "b": 0, "x": 16, "y": ll[1], "fmt": "BOA2_D  %7.2f [mT]"},
        {"label": "LIQ3_T", "a": 1.0, "b": 0, "x": 17, "y": ll[1], "fmt": "LIQ3_T  %7.2f [mT]"},
        {"label": "LIQ4_T", "a": 1.0, "b": 0, "x": 18, "y": ll[1], "fmt": "LIQ4_T  %7.2f [mT]"},
        # Check sum
        {"label": "CSUM", "a": 1, "b": 0, "x": 20, "y": ll[0], "fmt": "CSUM        %02X [hex]"}
    ]
