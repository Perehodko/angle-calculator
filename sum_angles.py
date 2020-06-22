fname = input("Enter file name: ")
if len(fname) < 1: fname = "test_sum.txt"

fh = open(fname)
store_list = []
count = 0
for line in fh:
    line_r = line.rstrip()
    print("   ", line_r)


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
    if count == 2:
        sum_ang = store_list[0]+store_list[1]
        store_list = []
        count = 0

        #ang
        ang = int(sum_ang)
        #min
        min_tenth = sum_ang - ang
        min = min_tenth * 60
        if min >= 60:
            ang += 1
            min -= 60
        #sec
        sec_tenth = min - int(min)
        sec = sec_tenth * 60
        if sec >= 60:
            min += 1
            sec -= 60
        if sum_ang >= 360:
            sum_ang -= 360
            print("-->", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), int(min), round(sec)))
        else:
            # sum
            print("-->", "{0}ᵒ{1}'{2}\"".format(int(sum_ang), int(min), round(sec)))
