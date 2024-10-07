# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator=="+":
    print(f"Summation of {num1} and {num2} is : ", num1 + num2)
elif operator=="-":
    print(f"Subtraction of {num1} and {num2} is : ", num1 - num2)
elif operator=="*":
    print(f"Multiplication of {num1} and {num2} is : ", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(f"Division of {num1} and {num2} is : ", num1 / num2)
    else:
        print("Undefined: Divisor cannot be zero")
else:
    print(f"{operator} is not a valid operator")

