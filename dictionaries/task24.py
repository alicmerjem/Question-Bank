"""
what is printed by the following 
statements?
"""
total = 0
thedict = {"apolo": 22, "orlando": 36, "qwerty": 23, "notafruit": 17}
for akey in thedict:
    if len(akey) > 5:
        total = total + thedict[akey]
print(total)
print("charlie" in thedict)
print(23 in thedict)

"""
98
False
True
"""