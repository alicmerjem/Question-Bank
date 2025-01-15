"""
given a string, write a function to 
return a new string made of 3 copies
of the last 2 chars of the original
string. the string length will be 
at least 2 
"""
def extra_end(word):
    last_two = word[-2:]
    return last_two * 3

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))