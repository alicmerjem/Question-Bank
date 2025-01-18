"""
what is printed by the following
statements?
"""

thedict = {"aap": 4, "ole": 6, "en": 13, "fr": 77}
thedict["rex"] = thedict["aap"] + thedict["fr"]
thedict["cop"] = thedict["ole"] + thedict["en"]
print(thedict["rex"])

for akey in thedict.keys():
    print("key", akey, "maps to", thedict[akey])

ahalist = list(thedict.keys())
print(ahalist)
ahalist.sort()
print(ahalist[-2] + ahalist[-1])


"""
81
key aap maps to 4
key ole maps to 6
key en maps to 13
key fr maps to 77
key rex maps to 81
key cop maps to 19
['aap', 'ole', 'en', 'fr', 'rex', 'cop']
rexcop
"""