# Count the number of vowels in a given string.

def countvowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = input("enter something: ")
print(countvowels(input_string))

