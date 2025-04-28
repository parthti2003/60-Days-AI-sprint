# Sum of numbers from 1 to N using while loop.
n = int(input("Enter a number: "))
a = 1
total = 0  # to store the sum

while a <= n:
    total += a   # Add 'a' to 'total'
    a += 1       # Move to next number

print("Sum is:", total)
