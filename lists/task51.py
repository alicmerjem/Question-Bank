"""
write a function to reverse strings in
a given list of string values
"""
def reverse_str(strings):
    return [string[::-1] for string in strings]

strings = ['red', 'blue', 'green', 'orange']
print(reverse_str(strings))