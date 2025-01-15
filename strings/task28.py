"""
write a function to add ing at the end
of a given string (len shall be at least
3). if the given string already ends 
with ing then add ly instead. if the
string len of the given string is less
than 3, leave it unchanged
"""

def something(s):
    if len(s)>=3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    return s

print(something('abc'))
print(something('string'))
print(something('s'))