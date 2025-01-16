"""
write a python function to find a list
of words that are longer than n from
a given list of words
"""
def longer(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

list = ['apple', 'bananan', 'orange', 'kiwi', 'watermelon']
n = 5
print(longer(list, n))