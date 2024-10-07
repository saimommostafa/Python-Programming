weight = int(raw_input("Weight: "))
unit = raw_input("(L)bs or (K)g: ")

if unit.upper() == 'K':
    conv = weight / 0.45
    print "You are", conv, "pounds"
else:
    conv = weight * 0.45
    print "You are", conv, "kilos "