import module1 as m1
import module2 as m2
# Reuse the is_prime function from module1

# Check if the digit sum is prime
if m1.is_prime(m2.digit_sum):
    print(f"The digit sum {m2.digit_sum} is a prime number.")
else:
    print(f"The digit sum {m2.digit_sum} is not a prime number.")
