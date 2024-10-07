price = 1000000
gc = True

if gc:
    down_payment = .1 * price

else:
    down_payment = .2 * price
print "Down payment: $" + str(down_payment)





name = "Saimom"

if len(name) < 3: 
    print "Name must be at least 3 characters"
elif len(name) > 10:
    print "Name can be maximum 10 characters"
else:
    print "Name looks good"