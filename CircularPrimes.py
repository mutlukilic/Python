def isprime(a):
    ###bir sayýnýn asal olup olmadýðýný kontrol eden fonksiyon
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
sonuc = 13
for n in range(101,1000,2):
    if(isprime(n)==0):
        continue
    for p in range(len(str(n))):
        if(isprime(int(n))==0):
            break
        n=list(str(n))
        n.append(n[0])
        n.remove(n[0])
        n=''.join(str(i) for i in n)
    else:
        sonuc +=1
print(sonuc)
