import math
import decimal

fname = input("Enter file name: ")
if len(fname) < 1: fname = "test_data.txt"

fh = open(fname)

for line in fh:
    line_r = line.rstrip()

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
        sec_to_min = int(sec) / 60

        min_plus_sec = float(minute) + sec_to_min

        # only degree
        degree = float(angler) + float(minute) / 60 + float(sec) / 3600
        # radians
        radians = (float(degree) * math.pi) / 180
        # БДУ
        GD = float(degree) / 6

        if "." in angler:
            # ANGLER int
            ang_int = int(float(angler))
            # десятая градуса
            ang_tenth = round((float(angler) - ang_int), 4)
            # получаю минуты из десятых градуса
            minute_from_ang_tenth = ang_tenth * 60

            minute_tenth =  minute_from_ang_tenth - int(minute_from_ang_tenth)
            sec_from_min = minute_tenth * 60
            if sec_from_min >= 60:
                 minute_from_ang_tenth += 1
                 sec_from_min = 0
            # print("gd", GD, "ang_int",ang_int, "angler:", angler,"ang_tenth:", ang_tenth,"minute_tenth:", minute_tenth,"minute_form_ang_tenth:", minute_from_ang_tenth,"sec_from_min:", sec_from_min)

            print("=" * 40, sep='\n')
            # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
            print("original str:", line_r)
            print("-" * 40)
            print("            degree -->", '%.5f' % degree)
            print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(ang_int, int(minute_from_ang_tenth), int(math.ceil(sec_from_min*100)/100)))
            print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(ang_int, (math.ceil(minute_from_ang_tenth*100)/100)))

            print("           radians -->", '%.1f' % radians)
            print("               GD --> ", str(math.ceil(GD*100)/100).replace(".", "-"))
            continue

        elif "." in minute:
            # ANGLER
            ang = int(float(angler))
            # MINUTES
            minutes = int(float(minute))
            min_tenth = float(minute) - minutes

            min_f = minutes + min_tenth

            sec_from_min_tenth = min_tenth * 60

            print("=" * 40, sep='\n')
            # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
            print("original str:", line_r)
            print("-" * 40)
            print("            degree -->", '%.5f' % degree)
            print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(ang, int(minutes), int(sec_from_min_tenth)))
            print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(ang, min_f))
            print("           radians -->", '%.1f' % radians)
            # print("                GD -->", str(math.ceil(GD*100)/100).replace(".", "-"))
            print("                GD -->", (str(round(GD, 2)).replace(".", '-')))
            continue


        print("=" * 40, sep='\n')
        # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
        print("original str:", line_r)

        print("-" * 40)
        print("            degree -->", '%.5f' % degree)
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(angler, minute, sec))
        print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(angler, math.ceil(min_plus_sec*100)/100))
        print("           radians -->", '%.2f' % radians)
        GD_i = str(round(GD, 2))
        GD_i = GD_i.replace(".", "-")
        print("                GD -->", GD_i)

    if "-" in line_r:
        # float from GD
        num = float(line_r.replace('-', '.'))
        angler_from_GD = num * 6
        #float минуты
        min_f_from_GD = angler_from_GD - int(angler_from_GD)

        min_from_GD = min_f_from_GD * 60
        # целые минуты
        int_min_GD = int(min_from_GD)
        #доли минут для перевода в секунды
        min_GD_float = min_from_GD - int_min_GD
        #перевод долей градуса в секунды
        sec_GD = min_GD_float * 60

        if math.ceil(sec_GD*100)/100 >= 60:
            int_min_GD += 1
            sec_GD = 0
        # минуты с долями
        min_sec = int_min_GD + sec_GD / 60
        # print(min_from_GD, int_min_GD, min_GD_float, sec_GD, min_sec)

        # radians
        radians_GD= (float(angler_from_GD) * math.pi) / 180

        # print('!!!')
        print("=" * 40, sep='\n')
        print("original str:", line_r)
        print("-" * 40)
        print("            degree -->", '%.5f' % angler_from_GD)
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(angler_from_GD), int_min_GD, int(float(sec_GD))))
        print("   mask 000ᵒ00.00' -->", "{0}ᵒ{1}'".format(int(angler_from_GD), round(min_sec, 2)))
        print("           radians -->", '%.2f' % radians_GD)
        print("                GD -->", line_r)



