"""
given a string, write a function to
return a version without the first and 
last char, so hello yields ell. the 
string length will be at least 2
"""
def without_end(s):
    return s[1:-1]

print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))