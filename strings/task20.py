"""
given a string, write a function to 
return a string where for every char
in the original three are two chars
"""
def double_char(s):
    return ''.join([char * 2 for char in s])

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))