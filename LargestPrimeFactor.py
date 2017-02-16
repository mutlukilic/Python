from functions import allprimes

primes = allprimes(18)
number,i = 40,1
while not (number % primes[-i] == 0):
    i += 1
print(primes[-i])
