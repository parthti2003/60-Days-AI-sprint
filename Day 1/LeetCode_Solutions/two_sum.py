class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store numbers we've already seen
        for i, num in enumerate(nums):  # Loop through the list with both index and value
            complement = target - num  # Calculate the complement (what we need to reach target)
            
            # Check if the complement already exists in the dictionary
            if complement in seen:
                return [seen[complement], i]  # Return indices of the complement and current number
            
            # If not found, add the current number and its index to the dictionary
            seen[num] = i
        
        return []  # If no solution is found
