import math
fname = input("Enter file name: ")
if len(fname) < 1: fname = "test_data_with_point.txt"

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
        # only degree
        degree = float(angler) + float(minute) / 60 + float(sec) / 3600
        # radians
        radians = (float(degree) * math.pi) / 180
        # БДУ
        GD = float(degree) / 6

        if "." in angler:
            # ANGLER
            ang = int(float(angler))
            # десятая градуса
            ang_tenth = float(angler) - ang
            minute_from_ang_tenth = ang_tenth * 60
            minute_tenth = minute_from_ang_tenth - int(minute_from_ang_tenth)
            sec_from_min = round(minute_tenth,2) * 60
            if sec_from_min >= 60:
                minute_from_ang_tenth += 1
                sec_from_min = 0
            # print(minute_tenth, minute_from_ang_tenth, sec_from_min)

            print("=" * 40, sep='\n')
            # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
            print("original str:", line_r)
            print("-" * 40)
            print("            degree -->", '%.5f' % degree)
            print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(ang, int(minute_from_ang_tenth), int(sec_from_min)))
            print("mask 000ᵒ00'00.00\" -->",
                  "{0}ᵒ{1}'{2}.{3}\"".format(ang, int(minute_from_ang_tenth), int(sec_from_min), "00"))

            print("           radians -->", '%.1f' % radians)
            GD_i = str(GD).find(".")
            print("                GD -->", "{0}-{1}".format(int(GD), str(GD)[GD_i + 1:GD_i + 3:]))

        elif "." in minute:
            # ANGLER
            ang = int(float(angler))
            # MINUTES
            minutes = int(float(minute))
            min_tenth = float(minute) - minutes
            sec_from_min_tenth = min_tenth * 60

            print("=" * 40, sep='\n')
            # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
            print("original str:", line_r)
            print("-" * 40)
            print("            degree -->", '%.5f' % degree)
            print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(ang, int(minutes), int(sec_from_min_tenth)))
            print("mask 000ᵒ00'00.00\" -->",
                  "{0}ᵒ{1}'{2}\"".format(ang, int(minutes), round(sec_from_min_tenth, 2)))
            print("           radians -->", '%.1f' % radians)
            GD_i = str(GD).find(".")
            print("                GD -->", "{0}-{1}".format(int(GD), str(GD)[GD_i + 1:GD_i + 3:]))
            # print(min_tenth, sec_from_min_tenth)


