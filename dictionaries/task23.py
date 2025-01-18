"""
what is printed by the following
statements?
"""
total = 0
thedict = {"ap": 2, "do": 6, "ty": 3, "fruit": 17}
for akey in thedict:
    if len(akey) > 5:
        total = total + thedict[akey]
print(total)
print("rex" in thedict)
print(22 in thedict)

"""
17
False
False
"""