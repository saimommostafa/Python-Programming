for x in range(4):
    for y in range(3):
        print('(%d, %d)') % (x, y)

num = [6, 2, 4, 2, 6]
for x_count in num:
    output = ''
    for count in range(x_count):
        output += 'x'
    print output