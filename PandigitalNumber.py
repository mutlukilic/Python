def is_Pandigital(nr,n):
    digits = ''.join(map(str,range(1,n+1)))
    nr = str(nr)
    for i in digits:
        if i not in nr[0:n]:
            return False
    return True

toplam = 0
n = input("n degerini giriniz : ")
for i in range(100,1000):
    if is_Pandigital(i,n):
        toplam += i
print toplam
