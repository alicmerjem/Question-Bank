"""
write a function to sum all amicable
numbers from 1 to specified numbers.
note: amicable numbers are two
different numbers so realted that the
sum of the proper divisors of each is 
equal to the other number. 
a proper divisor is a positive factor
of that number other than the number
itself. e.g. the proper divisors of 6
are 1, 2 and 3
"""
def amicable_numbers_sum(limit):
    def get_divisors_sum(n):
        return sum(i for i in range(1, n) if n%i==0)
    total = 0
    for i in range(1, limit +1):
        div_sum_i = get_divisors_sum(i)
        if div_sum_i != i and get_divisors_sum(div_sum_i) == i:
            total += i
    return total


print(amicable_numbers_sum(9999))
print(amicable_numbers_sum(999))
print(amicable_numbers_sum(99))