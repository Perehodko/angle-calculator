import math

fname = input("Enter file name: ")
if len(fname) < 1: fname = "test_multi_sum.txt"

fh = open(fname)
numbers_list = []

global angler, minute, num

for line in fh:
    line_r = line.rstrip()
    if not line_r.isspace():
        print("   ", line_r)
        if "ᵒ" in line_r:
            # sign
            sign = line_r[0:1]
            # print(sign)
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
            if sign == "-" and float(angler) == 0:
                d1 = - d1
            numbers_list.append(d1)
        elif "-" in line_r:
            num_s = (line_r.replace('-', '.'))
            # print(num_s)
            num = float(num_s)
            angler_from_GD = num * 6
            d1 = angler_from_GD
            numbers_list.append(d1)
        else:
            # print(numbers_list)
            sum_ang = sum(numbers_list)
            numbers_list = []

            # ang
            ang = int(sum_ang)
            # min
            min_tenth = sum_ang - ang
            min = min_tenth * 60

            # sec
            sec_tenth = min - int(min)
            sec = sec_tenth * 60
            if sec >= 60:
                min += 1
                sec -= 60

            if min >= 60:
                sum_ang += 1
                min -= 60
            elif min < 0:
                min = 60 - abs(min)
                # sum_ang -= 1

            while sum_ang >= 360:
                sum_ang -= 360
            if sum_ang < 0:
                sum_ang = 360 - abs(sum_ang)

            # radians
            radians = (float(sum_ang) * math.pi) / 180

            # БДУ
            GD = float(sum_ang) / 6
            if round(GD, 2) == 60:
                GD = 00.00

            print("-" * 35)
            if "." in angler:
                print("res", '%.5f' % sum_ang)
            elif "." in minute:
                print("res", "{0}ᵒ{1}'".format(int(sum_ang), round(min, 2)))
            else:
                print("res", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), int(min), round(sec)))
            # else:
            #     print("res", (str(round(GD, 2)).replace(".", '-')))

            print("-" * 35)
            print("            degree -->", '%.5f' % sum_ang)
            print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), round(min), round(float(sec))))
            print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(sum_ang), round(min, 2)))
            print("           radians -->", '%.2f' % radians)
            print("                GD -->", (str(round(GD, 2)).replace(".", '-')))
            print("=" * 35, sep='\n')
            print("\n")




