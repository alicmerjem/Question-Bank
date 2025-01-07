"""
write a function to compute the sum of
first n given prime numbers
"""

def sum_prime(n):
    primes = []
    num = 2
    while len(primes)<n:
        for i in range(2, int(num**0.5) + 1):
            if num%i==0:
                break
            else:
                primes.append(num)
        num+=1
    return sum(primes)