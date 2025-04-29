# Write a Python program to find the second largest number in a list.


def find_second_largest(nums):
    if len(nums) < 2:
        return "List must have at least 2 elements."

    max1 = max2 = float('-inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    if max2 == float('-inf'):
        return "No second largest found (all elements same?)"
    
    return max2

# Test
print(find_second_largest([5, 3, 9, 1, 6]))  
