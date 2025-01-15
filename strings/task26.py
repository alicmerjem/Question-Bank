"""
write a function to get a string from
a given string where all occurences of
its first char have been changed to $
except the first char itself
"""
def change_char(s):
    return s[0] + s[1:].replace[s[0], '$']

print(change_char('restart'))