"""
filter even numbers from dict values
"""

def filter_even_numbers(dictionary):
    return {key: [x for x in value if x%2==0] for key, value in dictionary.items()}

data = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
print(filter_even_numbers(data))