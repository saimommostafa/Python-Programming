#Variables 

name = 'Saimom Mostafa Emon'
age = 18 #according to birth certificate
height = 63 #inch
weight = 49 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'
height_cm = 2.54 * height
weight_lbs = 2.2046 * weight

print "Let's talk about %s." %name
print "He's %d inches or %r cm tall." %(height, height_cm)
print "He's %d kg heavy." %weight
print "Actually that's not too heavy, only %f pounds." %weight_lbs
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)