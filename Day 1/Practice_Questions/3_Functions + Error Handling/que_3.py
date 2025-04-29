# Write a function that checks if a string is palindrome.

def isPalindrome(s):

    s = s.replace(" ","").lower()
    return s == s[::-1] #this reverses the string

s = input()
print(isPalindrome(s))