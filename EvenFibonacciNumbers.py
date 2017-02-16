a,b,c,toplam = 1,1,0,0
while c < 100:
    if c % 2 == 0: toplam += c
    c = a+b
    a,b = b,c
print (toplam)
