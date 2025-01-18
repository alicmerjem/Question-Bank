"""
what is printed by the following
statements?
"""
total = 0
mydict = {"apple": 13, "orange": 16, "plum": 23, "grapefruit": 17}
for akey in mydict:
    if len(akey) > 4:
        total = total + mydict[akey]
print(total)
print("orange" in mydict)
print(23 in mydict)

"""
46
True
False
"""