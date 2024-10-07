import module1


# Function to sum the digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Use the result from step 1 (prime_sum)
digit_sum = sum_of_digits(module1.prime_sum)

print("Sum of digits of the prime sum:", digit_sum)
