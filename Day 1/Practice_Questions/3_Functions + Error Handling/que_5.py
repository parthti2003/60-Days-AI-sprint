# Try intentionally raising and handling a ZeroDivisionError.

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: You tried to divide by zero!")

# Try dividing by zero
divide_numbers(10, 0)
