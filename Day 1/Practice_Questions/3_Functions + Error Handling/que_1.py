# Write a function to return the maximum of two numbers.
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Example use
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum is:", find_max(x, y))
