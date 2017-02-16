def isPerfectNumber(number):
    division_sum = 0
    for i in range(1,number/2+1):
        if ( number % i == 0):
            division_sum += i
    if(division_sum == number): return 1
    return 0

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

def ispandigital(n):
    """bir sayýnýn pandigital sayý olup olmadýðýný kontrol eden fonksiyon"""
    number = []
    for i in str(n):
        number.append(int(i))
    for i in range(1,len(number)+1):
        if(number.count(i)==0):
            return(0)
    else:
        return(1)

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

def divisors(n):
    """bir sayýnýn bölenlerini bir dizi olarak geri döndüren fonksiyon"""
    carpanlar = [1]
    i=2
    while (i<=n/2):
        if n%i==0:
            carpanlar.append(i)
        i += 1
    return(carpanlar)
