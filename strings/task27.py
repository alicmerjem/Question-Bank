"""
write a function to get a single string
from two given strings, separated by 
a space and swap the first two 
characters of each string
"""
def swap_chars(s1, s2):
    return s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]

print(swap_chars('abc', 'xyz'))