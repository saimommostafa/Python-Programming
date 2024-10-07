from sys import argv

script, x = argv
b = open(x, 'w+b')
print b.write('emon/')
print b.read()