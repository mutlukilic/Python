def allprimes(n):
    """bir sayýdan küçük bütün asal sayýlarý dizi olarak döndüren fonksiyon"""
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])

LIMIT = 100
primes = allprimes(LIMIT)
sonuc = 0

for i in range(1, len(primes)):
    p = primes[i]
    for j in range(i):
        q = primes[j]
        l = int(LIMIT/q)
        if l < p:
            break
        r = p
        liste = []
        while r <= l:
            s = r*q
            while(s <= LIMIT):
                s *= q
            liste += [int(s/q)]
            r *= p
        sonuc += max(liste)

print(sonuc)
