import math
import decimal as decimal

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
            # print("sum", sum_ang)
            if sum_ang >= 0:
                numbers_list = []

                # ang
                ang = int(sum_ang)
                # min
                # print("ang", ang)
                min_tenth = sum_ang - abs(ang)
                min = min_tenth * 60
                # print("min", min, min_tenth)

                # sec
                sec_tenth = min - abs(int(min))
                # print("sec_tenth", sec_tenth)
                sec = sec_tenth * 60
                sec = round(sec,4)
                # print(angler, min,sec)
                if sec >= 60:
                    min += 1
                    sec -= 60
                    print("1")
                elif sec < 0:
                    sec = 60 - abs(sec)
                    if sec < 0:
                        sec = 60 - abs(sec)
                    min += 1
                    # print("2")
                # print(sec)


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
                    print("res", "{0}ᵒ{1}'".format(int(sum_ang), min))
                else:
                    print("res", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), int(min), round(sec)))
                # else:
                #     print("res", (str(round(GD, 2)).replace(".", '-')))

                print("-" * 35)
                print("            degree -->", '%.5f' % sum_ang)
                print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), int(min), round(float(sec))))
                print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(sum_ang), round(min, 2)))
                print("           radians -->", '%.2f' % radians)
                print("                GD -->", (str(round(GD, 2)).replace(".", '-')))
                print("=" * 35, sep='\n')
                print("\n")
            elif sum_ang < 0:
                numbers_list = []
                res = 360 - abs(sum_ang)
                # print(res)
                # ang
                ang = int(res)
                # min
                min_tenth = res - abs(ang)
                min = min_tenth * 60
                # print("min", min, min_tenth)

                # sec
                sec_tenth = min - abs(int(min))
                # print("sec_tenth", sec_tenth)
                sec = round(sec_tenth * 60+0.01, 2)
                # sec_round = round(sec + 0.01,3)
                # print(angler, min,sec)
                if sec < 0:
                    sec = 60 - abs(sec)
                elif sec == 60:
                     sec = 0
                     min += 1
                elif sec > 60:
                    sec = sec - 60
                    min += 1
                    min = float(int(min))

                if min > 60:
                    ang -= 1
                    min = 60 - abs(min)
                if min < 0:
                    min = 60 - abs(min)

                # print(angler, min,sec)

                # radians
                radians = abs(float(res) * math.pi) / 180

                # БДУ
                GD = float(res) / 6
                if round(GD+0.0001, 2) == 60:
                    GD = 00.00

                min_round = round(min + 0.0001, 2)

                print("-" * 35, sep='\n')
                if "." in angler:
                    print("res", '%.5f' % res)
                elif "." in minute:
                    print("res", "{0}ᵒ{1}'".format(int(ang), int(min)))
                else:
                    print("res", "{0}ᵒ{1}'{2}\"".format(int(ang), int(min), int(float(sec))))
                print("-" * 35, sep='\n')
                print("            degree -->", '%.5f' % res)
                print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(ang), int(min), int(sec)))
                print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(ang), round(min, 2)))
                print("           radians -->", '%.2f' % radians)
                print("                GD -->", (str(round(GD+0.0001, 2)).replace(".", '-')))
                print("-" * 35, sep='\n')
                print("\n")