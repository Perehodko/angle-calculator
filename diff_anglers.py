import math

fname = input("Enter file name: ")
if len(fname) < 1: fname = "test_diff.txt"

fh = open(fname)
store_list = []
count = 0
for line in fh:
    line_r = line.rstrip()
    if not line_r.isspace():
        print("   ", line_r)
        if count == 0:
            print("-" * 35)

    if "ᵒ" in line_r:
        # pos ang
        pos_angl = line_r.find("ᵒ")
        angler = line_r[:pos_angl]
        # pos minute
        pos_minute = line_r.find("'")
        minute = line_r[pos_angl + 1:pos_minute]
        # sec
        pos_sec = line_r.find("\"")
        sec = line_r[pos_minute + 1:pos_sec]

        d1 = float(angler) + (float(minute) * 0.0166666667) + (float(sec) * 0.000277778)
        store_list.append(d1)
        count += 1
    if "-" in line_r:
        # float from GD
        num = float(line_r.replace('-', '.'))
        angler_from_GD = num * 6

        d1 = angler_from_GD
        store_list.append(d1)
        count += 1

    if count == 2 and "ᵒ" in line_r:
        diff_ang = store_list[0] - store_list[1]
        store_list = []
        count = 0

        # ang
        ang = int(diff_ang)
        # min
        min_tenth = diff_ang - ang
        min = min_tenth * 60
        if min > 60:
            ang -= 1
            min = 60 - abs(min)

        # sec
        sec_tenth = min - int(min)
        sec = sec_tenth * 60
        # if sec < 60:
        #      min -= 1
        #      sec = 60 - abs(sec)

        if diff_ang < 0:
            # print(diff_ang)
            diff_ang = 360 - abs(diff_ang)
        if min < 0:
            min = 60 - abs(min)
        if sec < 0:
            sec = 60 - abs(sec)

        # radians
        radians = (float(diff_ang) * math.pi) / 180

        # БДУ
        GD = float(diff_ang) / 6

        print("-" * 35, sep='\n')
        print("diff", "{0}ᵒ{1}'{2}\"".format(int(diff_ang), int(min), int(float(sec))))
        print("-" * 35, sep='\n')
        print("            degree -->", '%.5f' % diff_ang)
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(diff_ang), int(min), int(float(sec))))
        print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(diff_ang), round(min, 2)))
        print("           radians -->", '%.2f' % radians)
        print("                GD -->", (str(round(GD, 2)).replace(".", '-')))
        print("-" * 35, sep='\n')
        print("\n")
    if count == 2 and "-" in line_r:
        diff_ang = store_list[0] - store_list[1]
        # print(diff_ang)
        if diff_ang < 0:
            diff_ang = 360 - abs(diff_ang)
            # print(diff_ang)

        diff_ang_GD = diff_ang / 6
        store_list = []
        count = 0
        # float минуты
        min_f_from_GD = diff_ang - int(diff_ang)

        min_from_GD = min_f_from_GD * 60
        # целые минуты
        int_min_GD = int(min_from_GD)
        # доли минут для перевода в секунды
        min_GD_float = min_from_GD - int_min_GD
        # перевод долей градуса в секунды
        sec_GD = min_GD_float * 60

        if math.ceil(sec_GD * 100) / 100 >= 60:
            int_min_GD += 1
            sec_GD = 0
        # минуты с долями
        min_sec = int_min_GD + sec_GD / 60
        # print(angler_from_GD)

        # radians
        radians_GD = (float(diff_ang) * math.pi) / 180

        print("-" * 35, sep='\n')
        # print("original str:", line_r)
        print("diff", (str(round(diff_ang_GD, 2)).replace(".", '-')))
        print("-" * 35)
        print("            degree -->", '%.5f' % diff_ang)
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(diff_ang), int_min_GD, int(float(sec_GD))))
        print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(diff_ang), round(min_sec, 2)))
        print("           radians -->", '%.2f' % radians_GD)
        print("                GD -->", (str(round(diff_ang_GD, 2)).replace(".", '-')))
        print("-" * 35, sep='\n')
        print("\n")
