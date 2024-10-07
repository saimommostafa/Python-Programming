def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

def me(name, age, hometown):
    print 'Name:', name
    print 'Age:', age 
    print 'Hometown:' , hometown, '\n'

me('Saimom'+'Emon', 18, 'Barguna')

me('Emon', 18+1, 'Barguna')

me('Emon', 18, 'Barguna Sadar')

me('Reon', 18+1, 'Dhaka')

me('Esmita', 13, 'Barguna')

me('Emon', 18, 'Barguna')


def c_a_c(cheeses= int(raw_input('No. of cheeses:')), crackers= int(raw_input('No. of crackers:'))):
    print 'Cheeses:', cheeses
    print 'Crackers:', crackers
    print 'Total:', cheeses+crackers
    
c_a_c()
