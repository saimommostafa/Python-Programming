p = open('encrypted.txt')
q = p.read()
decr = [""]
for dec in q:
    if dec == 'Z':
        decr[0] += 'a'
    elif dec == 'Y':
        decr[0] += 'b'
    elif dec == 'X':
        decr[0] += 'c'
    elif dec == 'W':
        decr[0] += 'd'
    elif dec == 'V':
        decr[0] += 'e'
    elif dec == 'U':
        decr[0] += 'f'
    elif dec == 'T':
        decr[0] += 'g'
    elif dec == 'S':
        decr[0] += 'h'
    elif dec == 'R':
        decr[0] += 'i'
    elif dec == 'Q':
        decr[0] += 'j'
    elif dec == 'P':
        decr[0] += 'k'
    elif dec == 'O':
        decr[0] += 'l'
    elif dec == 'N':
        decr[0] += 'm'
    elif dec == 'M':
        decr[0] += 'n'
    elif dec == 'L':
        decr[0] += 'o'
    elif dec == 'K':
        decr[0] += 'p'
    elif dec == 'J':
        decr[0] += 'q'
    elif dec == 'I':
        decr[0] += 'r'
    elif dec == 'H':
        decr[0] += 's'
    elif dec == 'G':
        decr[0] += 't'
    elif dec == 'F':
        decr[0] += 'u'
    elif dec == 'E':
        decr[0] += 'v'
    elif dec == 'D':
        decr[0] += 'w'
    elif dec == 'C':
        decr[0] += 'x'
    elif dec == 'B':
        decr[0] += 'y'
    elif dec == 'A':
        decr[0] += 'z'
    elif dec == 'a':
        decr[0] += '@'
    elif dec == 'h':
        decr[0] += '-'
    elif dec == 's':
        decr[0] += ' '
    elif dec == 'p':
        decr[0] += '.'
    elif dec == '9':
        decr[0] += '0'
    elif dec == '8':
        decr[0] += '1'
    elif dec == '7':
        decr[0] += '2'
    elif dec == '6':
        decr[0] += '3'
    elif dec == '5':
        decr[0] += '4'
    elif dec == '4':
        decr[0] += '5'
    elif dec == '3':
        decr[0] += '6'
    elif dec == '2':
        decr[0] += '7'
    elif dec == '1':
        decr[0] += '8'
    elif dec == '0':
        decr[0] += '9'
    elif dec == '#':
        print('\n')
    elif dec == '*':
        decr[0] += '&'
    else:
        decr[0] += '?'
    print decr[0]
    
p.close()