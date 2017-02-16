from math import factorial
"""def factorial(n):
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    return(factorial)
sonuc = 0
for n in range(3,100000):
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    if(toplam == n):
        sonuc += n
print(sonuc)"""
sonuc = 0
for n in range(3,100000):
    toplam = 0
    for i in str(n):
        toplam += factorial(int(i))
    if n==toplam:
        sonuc += n
print(sonuc)
