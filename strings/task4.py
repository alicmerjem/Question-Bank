"""
we will say that a triple in a string
is a character appearing three times
in a row. write a function that returns
the number of triples in the given string.
the triples may overlap.
"""
def countTriple(s):
    return sum(1 for i in range(len(s)-2) if s[i] == s[i+1] == s[i+2])

print(countTriple("abcXXXabc"))
print(countTriple("xxxabyyyycd"))
print(countTriple("a"))