# Simple Calculator App
# (Use input/output, functions, if/else)
# ➔ Take two numbers and an operation (+, -, *, /) as input and show the result.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = input("Enter the operation (+, -, *, /): ")

if c == "+":
    print(add(a, b))
elif c == "-":
    print(sub(a, b))
elif c == "*":
    print(multiply(a, b))
elif c == "/":
    print(divide(a, b))
else:
    print("Invalid operation.")
