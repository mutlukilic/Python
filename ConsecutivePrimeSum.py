def isprime(a):
    """bir sayýnýn asal olup olmadýðýný kontrol eden fonksiyon"""
    i,prime=3,1
    if(a<2):
        prime=0
    if a!=2 and a%2==0:
        prime=0
    while prime!=0 and i<=a**(1/2):
        if a%i==0:
            prime=0
            break
        i += 2
    return(prime)
maks = 1
primes = []
for i in range(2,1000000):
    if(isprime(i) == 1):
        primes.append(i)
for p in range(100,600):
    for i in range(len(primes)-p-1):
        sums = 0
        for j in range(p):
            sums += primes[i+j]
        if (i == 1) and sums > primes[-1]:
            break
        if(primes.count(sums) == 1):
            maks = sums
print(maks)
