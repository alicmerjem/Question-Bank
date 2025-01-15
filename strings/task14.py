"""
given a string, write a function to 
return the string made of its fist
two chars, so the string hello yields
he. if the string is shorter than len 2
return whatever there is, so x yields
x, and the empty string yields the 
empty string
"""
def first_two(s):
    return s[:2]

print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))