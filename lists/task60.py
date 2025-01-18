"""
write a functon to find common elements
in a given list of lists
"""

def common_elements(lists):
    # Start with the first list
    common = lists[0]
    
    # Check each element in the first list against the rest of the lists
    for element in common[:]:  # Use a copy of the list to iterate
        for lst in lists[1:]:
            if element not in lst:
                common.remove(element)
                break
    return common

# Example usage
lists1 = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
print(common_elements(lists1))  # Output: [2, 3]

lists2 = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print(common_elements(lists2))  # Output: ['c']
