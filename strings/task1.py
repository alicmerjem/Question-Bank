"""
write a function that for two given
strings prints all letters from the
first string that appear at least
twice in the second string
"""

def letters_in_second(s1, s2):
    for char in s1:
        if s2.count(char)>=2:
            print(char)