"""
write a function to split a list based
on the first character of a word
"""
def split_by_char(lst):
    result = {}

    for word in lst:
        first_char = word[0].lower()

        if first_char not in result:
            result[first_char] = []
        
        result[first_char].append(word)

    return result

sample = ['apple', 'banana', 'avocado', 'cherry', 'blueberry', 'grape']
print(split_by_char(sample))