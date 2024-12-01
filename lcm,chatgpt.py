# Function to calculate GCD using Euclidean algorithm
def gcd(a, b):
    while a:
        x = a
        a = b % a
        b = x
    return b

# Function to calculate LCM using the relationship with GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Input two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate and print the LCM
print(f"The Least Common Multiple (LCM) of {a} and {b} is: {lcm(a, b)}")
