"""
write a function to replace each 
character of a word of len five and 
more with hash character
"""

def function(s):
    words = s.split()

    modified_words = [word if len(word) < 5 else '#' * len(word) for word in words]

    return ' '.join(modified_words)

print(function('Count the lowercase letters in the said list of words'))