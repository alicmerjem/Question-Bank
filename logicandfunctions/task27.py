"""
write a function to find if a given
number is abundant. note: in number
theory, an abundant number or excessive
numbr is a number for which the sum of 
its proper divisors is greater than the 
number itself. the integer 12 is the
first abudnat number. its proper divisors
are 1, 2, 3, 4 and 6 for a total of 16
"""
def is_abundant(num):
    divisors = [i for i in range(1, num) if num%i==0]
    return sum(divisors)>num

print(is_abundant(12))
print(is_abundant(13))