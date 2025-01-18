"""
write a function to extract specified
size of strings from a given list
of string values
"""

def extract_strings(strings, length):
    return [string for string in strings if len(string) == length]

strings = ['Python', 'list', 'exercise', 'pracitce', 'solution']
print(extract_strings(strings, 8))