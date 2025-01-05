"""
How many times is the letter o
printed in the following statement?
"""

t = "landinafrica"
s = t[:-2] +t[1:]
for i in range(len(s)):
    if i%3==0:
        print(s[i])

"""
Zero times. The letter o doesn't
exist in the string.
"""