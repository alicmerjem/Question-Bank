"""
given 2 strings, write a function to
return theri concatenation, except 
omit the first char of each. the 
strings will be at least length 1
"""
def non_start(s1, s2):
    return s1[1:] + s2[1:]

print(non_start('Hello','There'))
print(non_start('java','code'))
print(non_start('shotl','java'))