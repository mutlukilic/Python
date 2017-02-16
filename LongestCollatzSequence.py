maks = []
for n in range(1,1000000):
    liste = []
    while n != 1:
        if(n % 2 != 0):
            n = 3*n+1
        else: n /= 2
        liste.append(n)
    maks.append(len(liste)+1)
print(maks.index(max(maks))+1)
