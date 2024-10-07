cities = ['Barishal', 'Dhaka', 'Khulna', 'Sylhet']
for city in cities:
    print (city)


age = [6,4,3,6,18,14,16,20,21,22,23,24,25,23,22,21,25,24,65,66]
count = 0
for a in age:
    if a>20:
        count += 1
print(f'Number of people having age more than 20 is: {count}')


child = 0
teen = 0
adult = 0
senior = 0
for b in age:
    if 0 < b <= 12:
        child += 1
    elif 12 < b <= 19:
        teen += 1
    elif 19 < b <= 64:
        adult += 1
    else:
        senior += 1
print("No. of Child: ",child, "\nNo. of Teen:", teen, "\nNo. of Adult:", adult, "\nNo. of Senior:", senior)