x= int(input("Enter your age:"))

if x>=0 and x<=12:
    print("Age group: Child")

elif x>12 and x<=19:
    print("Age group: Teen")

elif x>19 and x<=64:
    print("Age group: Adult")

else:
    print("Age group: Senior")