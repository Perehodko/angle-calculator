import math

fname =  input("Enter file name: ")
if len(fname) < 1 : fname = "test_data.txt"

fh = open(fname)

for line in fh:
    line_r = line.rstrip()

    #pos ang
    pos_angl = line_r.find("ᵒ")
    angler = line_r[:pos_angl]
    # pos minute
    pos_minute = line_r.find("'")
    minute = line_r[pos_angl+1:pos_minute]
    # sec
    pos_sec = line_r.find("\"")
    sec = line_r[pos_minute+1:pos_sec]
    # only degree
    degree = float(angler) + float(minute) / 60 + float(sec) / 3600
    #radians
    radians = (float(angler) * math.pi)/180
    # БДУ
    GD = float(angler) / 6
    print("="*40, sep='\n')
    # print("angler: " + angler, "minute: " + minute, "sec: "+ sec)
    print("original str:", line_r)

    print("-"*40)
    print("            degree -->" , '%.5f' %degree)
    if "." in angler:
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(int(float(angler)), minute, sec))
        print("mask 000ᵒ00'00.00\" -->", "{0}ᵒ{1}'{2}.{3}\"".format(int(float(angler)), minute, sec, "00"))
    elif "." in minute:
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(angler, int(float(minute)), sec))
        print("mask 000ᵒ00'00.00\" -->", "{0}ᵒ{1}'{2}.{3}\"".format(angler, int(float(minute)), sec, "00"))
    elif "." in sec:
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(angler, minute, int(float(sec))))
        print("mask 000ᵒ00'00.00\" -->", "{0}ᵒ{1}'{2}\"".format(angler, minute, float(sec)))
    else:
        print("   mask 000ᵒ00'00\" -->", "{0}ᵒ{1}'{2}\"".format(angler,minute,sec))
        print("mask 000ᵒ00'00.00\" -->", "{0}ᵒ{1}'{2}.{3}\"".format(angler,minute,sec, "00"))


    print("           radians -->", '%.2f' % radians)
    GD_i = str(GD).find(".")
    print("                GD -->", "{0}-{1}".format(int(GD), str(GD)[GD_i+1:GD_i+3:]))