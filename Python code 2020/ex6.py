x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# Also as- "Those who know " + str(binary) + " and those who " + str(do_not)

print x 
print y

print "I said: %r." % x
print "I also said: '%s'." % y 

hilarious = False #Boolean 
joke_evaluation = "Isn't that joke so funny?! %r"
# %r works in this line and shows the value of hilarious as string.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e