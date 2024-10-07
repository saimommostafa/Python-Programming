n = int(input("Enter how many numbers you want to input: "))
numbers = []

#for storing numbers in a list
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)


total = 0
#finding even numbers in the list and sum of even numbers
for even in numbers:
    if even%2 == 0:
        total += even
print(f"Sum of all even numbers: {total}")



#Removing the even numbers from the list

for rmv in numbers:
    if rmv % 2 == 0:
        numbers.remove(rmv)
print (f"List after removing even: {numbers}")


