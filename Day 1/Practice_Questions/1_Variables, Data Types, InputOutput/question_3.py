# Input two numbers from user and swap them without using a third variable.
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
a, b = b, a

print(f"a = {a}, b = {b}")