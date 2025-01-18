"""
write a function to calculate the 
product, multiplying all the numbers
of a given tuple
"""

def product_of_tuple(tup):
    product = 1
    for num in tup:
        product *= num
    return product

print(product_of_tuple(4, 3, 2, 2))
print(product_of_tuple(2, 4, 8, 8))