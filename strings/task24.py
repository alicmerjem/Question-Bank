"""
given two strings, write a function to
return true if either of the strings 
appears at the very end of the other
string. ignorning upper/lower case 
differences (in other words, the 
computation shall not be case sensitive)
note : s.lower() returns the lowercase
version of a string
"""
def end_other(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    return s1.endswith(s2) or s2.endswith(s1)

print(end_other('Hiabc','abc'))
print(end_other('AbC','HiaBc'))
print(end_other('abc','abXabc'))