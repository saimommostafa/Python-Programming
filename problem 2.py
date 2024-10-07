#Problem 2

name = input("Enter your name: ")
token = int(input("Enter your token number: "))

if token%2 == 1:
    print(f"{name}: your seat is confirmed")

elif token%2 == 0:
    print(f"{name}: you are in waiting list")

if token==0:
    print(f"Sorry! {name}: No seat available for you")
