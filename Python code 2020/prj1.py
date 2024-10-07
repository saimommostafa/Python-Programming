import random

stringLength = int(input("What word length do you want? [4-16]  ")) 


lines = open("n.txt").readlines(stringLength) 
line = lines[0] 

words = line.split() 
s = random.choice(words)

ran = range(4, 17)
if stringLength in ran:
    print 'Selecting a word...\n\n'
    print "Word: ", '*' * stringLength
else:
    print stringLength, 'is not an integer between 4 and 16'


chance = stringLength + 3

atmpt = 0
while atmpt < chance:
    print 'Attempts Remaining: ', chance
    chance -= 1
    
    guess = str(raw_input("Enter a letter: "))

    if guess in s:
        print """%s in word.
Enter next one--> \n""" % guess
    else:
        print '''You are wrong! 
Try again. \n'''
    atmpt += 1

print 'Word was - ', s