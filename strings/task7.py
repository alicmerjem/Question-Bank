"""
write a function that removes all
occurencess of a given letter from a 
string. if a given letter does not 
appear in the string, the remove the
first letter of the string
"""

def remove_letter(s, letter):
    if letter in s:
        return s.replace(letter, "")
    else:
        return s[1:]