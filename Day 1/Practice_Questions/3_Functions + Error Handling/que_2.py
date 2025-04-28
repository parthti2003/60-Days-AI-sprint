# Write a function to calculate factorial of a number.


def factorial(a):
    result = 1
    for i in range(a, 0, -1):  # From a to 1
        result *= i
    return result

a = int(input("enter your number: "))
print(factorial(a))
