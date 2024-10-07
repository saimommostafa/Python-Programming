from sys import argv
from os.path import exists

# takes 3 filename including this one as input
script, f_file, t_file = argv

print "Copying from %s to %s" %(f_file, t_file)

#we could do these two on line too, how?
in_file = open(f_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r " % exists(t_file)
print "Ready, hit E to continue, CTRL-C to abort."
raw_input('> ')

out_file = open(t_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
