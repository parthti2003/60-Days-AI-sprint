# Remove duplicates from a list using a set.

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
original_list = [1, 2, 3, 2, 4, 3, 5, 1]
unique_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List after removing duplicates:", unique_list)
