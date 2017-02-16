def isprime(n):
    for i in range(2,n):
        if(n%i == 0): return(0)
    return(1)
def allprimes(n):
    primes = []
    for i in range(2,n):
        if(isprime(i) == 1):
            primes.append(i)
    return(primes)
print(allprimes(10**7))
