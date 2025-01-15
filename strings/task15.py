"""
given a string of even len, write a 
function to return the first half. so
the tring woohoo yields woo
"""
def first_half(str):
    mid = len(str) // 2
    return str[:mid]

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))