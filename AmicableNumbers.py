def Amicable(x):
    toplam = 0
    for i in range(1,(x/2)+1):
        if(x%i == 0): toplam += i
    return(toplam)
toplam = 0
for i in range(1,10000):
    for j in range(i+1,10000):
        if(Amicable(i) == Amicable(j)):
            toplam += i
print(toplam)
