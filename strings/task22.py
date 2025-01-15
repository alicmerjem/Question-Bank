"""
write a function to return true if 
the string cat and dog appear the 
same number of times in the given 
string
"""
def cat_dog(string):
    return string.count('cat') == string.count('dog')

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))