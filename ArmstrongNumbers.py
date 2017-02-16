basamak_sayisi = input("Basamak sayisini giriniz : ")
for i in range(10**(basamak_sayisi-1),10**basamak_sayisi):
    armstrong = 0
    for j in str(i):
        armstrong += int(j)**basamak_sayisi
    if(armstrong == i):
        print(i)
