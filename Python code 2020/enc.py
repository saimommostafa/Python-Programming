a = open('e-mails.txt')
b = a.read()
encrypted = [""]
for enc in b:
    if enc == 'a':
        encrypted[0] += 'Z'
    elif enc == 'b':
        encrypted[0] += 'Y'
    elif enc == 'c':
        encrypted[0] += 'X'
    elif enc == 'd':
        encrypted[0] += 'W'
    elif enc == 'e':
        encrypted[0] += 'V'
    elif enc == 'f':
        encrypted[0] += 'U'
    elif enc == 'g':
        encrypted[0] += 'T'
    elif enc == 'h':
        encrypted[0] += 'S'
    elif enc == 'i':
        encrypted[0] += 'R'
    elif enc == 'j':
        encrypted[0] += 'Q'
    elif enc == 'k':
        encrypted[0] += 'P'
    elif enc == 'l':
        encrypted[0] += 'O'
    elif enc == 'm':
        encrypted[0] += 'N'
    elif enc == 'n':
        encrypted[0] += 'M'
    elif enc == 'o':
        encrypted[0] += 'L'
    elif enc == 'p':
        encrypted[0] += 'K'
    elif enc == 'q':
        encrypted[0] += 'J'
    elif enc == 'r':
        encrypted[0] += 'I'
    elif enc == 's':
        encrypted[0] += 'H'
    elif enc == 't':
        encrypted[0] += 'G'
    elif enc == 'u':
        encrypted[0] += 'F'
    elif enc == 'v':
        encrypted[0] += 'E'
    elif enc == 'w':
        encrypted[0] += 'D'
    elif enc == 'x':
        encrypted[0] += 'C'
    elif enc == 'y':
        encrypted[0] += 'B'
    elif enc == 'z':
        encrypted[0] += 'A'
    elif enc == '@':
        encrypted[0] += 'a'
    elif enc == '-':
        encrypted[0] += 'h'
    elif enc == ' ':
        encrypted[0] += 's'
    elif enc == '.':
        encrypted[0] += 'p'
    elif enc == '0':
        encrypted[0] += '9'
    elif enc == '1':
        encrypted[0] += '8'
    elif enc == '2':
        encrypted[0] += '7'
    elif enc == '3':
        encrypted[0] += '6'
    elif enc == '4':
        encrypted[0] += '5'
    elif enc == '5':
        encrypted[0] += '4'
    elif enc == '6':
        encrypted[0] += '3'
    elif enc == '7':
        encrypted[0] += '2'
    elif enc == '8':
        encrypted[0] += '1'
    elif enc == '9':
        encrypted[0] += '0'
    elif enc == '\n':
        encrypted[0] += '#'
    elif enc == '&':
        encrypted[0] += '*'
    else:
        encrypted[0] += '?'
    print encrypted[0]
    
a.close()