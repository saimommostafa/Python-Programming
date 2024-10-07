from sys import argv
script, in_f = argv

def p_all(f): 
    print f.read(), '\n'
    
def rewind(f):
    f.seek(0)
    
def print_a_line(l_count, f):
    print l_count, f.readline(),
    
c_file = open(in_f)

print "First let's print the whole file:\n"
p_all(c_file)

print "Now let's rewind, kind of like a tape.\n"
rewind(c_file)

print "Let's print 2 lines:"
c_line = 1
while c_line<=2:
    print_a_line(c_line, c_file)
    c_line += 1