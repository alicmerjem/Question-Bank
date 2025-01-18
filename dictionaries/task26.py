"""
yknow the drill
"""

tvoc = {"qw": 4, "en": 13, "fro": 77, "klo": 2}
tvoc["rex"] = tvoc["klo"] + tvoc["fro"] + tvoc["en"]
tvoc["str"] = tvoc["fro"] + tvoc["fro"]
print(tvoc["rex"])
for akey in tvoc.keys():
    print("key", akey, "maps to", tvoc[akey])

ahalist = list(tvoc.keys())
print(ahalist)
ahalist.sort()
print(ahalist[-2] + ahalist[-1])


"""
92
key qw maps to 4
key en maps to 13
key fro maps to 77
key klo maps to 2
key rex maps to 92
key str maps to 154
['qw', 'en', 'fro', 'klo', 'rex', 'str']
rexstr
"""