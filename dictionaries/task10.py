"""
print all unique values in a
dictionary
"""

def print_unique_values(data):
    unique_values = set()  # Use a set to automatically handle uniqueness
    for item in data:
        for value in item.values():
            unique_values.add(value)  # Add each value to the set
    print("Unique Values:", tuple(unique_values))

# Sample Data
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Call the function
print_unique_values(data)
