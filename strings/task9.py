"""
what is printed by the following
statements?
"""

aflist = ["ba", ["ab", "bc", "ad"], "bd"]

print(aflist[-2] + ["ad", "ad"])
print(aflist[1:] * 2)
print([aflist[-1] + ["af", "ag"]] * 2)

"""
1 - ["ab", "bc", "ad", "ad", "ad"]
2 - [["ab", "bc", "ad"], "bd", ["ab", "bc", "ad"], "bd"]
3 - TypeError: can only concatenate list (not "str") to list
"""