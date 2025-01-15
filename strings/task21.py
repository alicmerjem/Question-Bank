"""
write a function to return the number
of times that the string hi appears
anywhere in the given string
"""
def count_hi(s):
    return s.lower().count('hi')

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
print(count_hi('abch'))