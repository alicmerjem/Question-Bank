"""
How many times is the letter o
printed by the following statements?
"""

# first statement
s = "long long story"
for i in range(len(s)):
    if i % 3 == 0:
        print(s[i])

"""
Explanation: the string has 15
characters indexed from 0 to 14.
The loop iterates over each each 
index i and checks if its divisible
by 3. If it is, the character is
printed. Output:
l
g
o
o
r
So we have 2 o's. 
"""

# second part
t = " bonobo"
s = t[:-3] + t[1:3] + t[:5]
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])

"""
String t is bonobo. 
t[:-3] excludes last 3 chars -> bon
t[1:3] takes chars from 1 to 2 -> bo
t[:5] - from start until 4 -> bon
s = bon + bo + bon = bonbobo bon

After that loop through everything
and we get:
o
b

o
o
"""