# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to sum the digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


# Taking a list of integers as input from the user
num_list = list(map(int, input("Enter numbers separated by space: ").split()))

# Finding the sum of all prime numbers in the list
prime_sum = sum(num for num in num_list if is_prime(num))

print("Sum of prime numbers:", prime_sum)

# Use the result from step 1 (prime_sum)
digit_sum = sum_of_digits(prime_sum)

print("Sum of digits of the prime sum:", digit_sum)


# Function to sum the digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Use the result from step 1 (prime_sum)
digit_sum = sum_of_digits(prime_sum)

print("Sum of digits of the prime sum:", digit_sum)
