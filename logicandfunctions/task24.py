"""
write a function to count the number of
prime numbers less than a given non
negative number
"""
def number_of_primes(n):
    primes = [True] * n
    primes[0] = primes [1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return sum(primes)

print(number_of_primes(10))
print(number_of_primes(100))