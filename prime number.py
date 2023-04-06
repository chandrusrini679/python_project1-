# Write a program to find out the prime numbers

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# To find all prime numbers within a given range

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("Prime numbers in the range of {} to {} are:".format(start, end))

for number in range(start, end + 1):
    if is_prime(number):
        print(number)

# In this program, we first define a function is_prime that takes a number as input and returns True if it is a prime
# number, and False otherwise. To check if a number is prime, we iterate over all numbers from 2 to the square root
# of the number (since any factor of the number greater than its square root must be paired with a factor less than
# its square root), and check if the number is divisible by any of them. If it is, we return False; otherwise,
# we return True.

# We then prompt the user to enter the starting and ending numbers of the range within which we want to find all
# prime numbers. We then loop over all numbers in this range, and for each number, we use the is_prime function to
# check if it is prime. If it is, we print it out.



