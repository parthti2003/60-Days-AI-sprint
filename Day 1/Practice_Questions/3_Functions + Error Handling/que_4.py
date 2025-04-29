# Write a function that takes two numbers and returns their GCD.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48,122))