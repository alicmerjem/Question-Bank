"""
write a function to remove duplicate
words from a given list of strings
"""
def remove_duplicate(words):
    return list(dict.fromkeys(words))

words = ['python', 'something', 'something but different', 'python']
print(remove_duplicate(words))