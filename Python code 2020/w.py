import random

lines = open("n.txt").readlines() 
line = lines[0] 

words = line.split() 
myword = random.choice(words)
print myword



def randomString(a):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) 
    for i in range(stringLength))
        