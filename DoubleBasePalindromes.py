def ispalindrome(n):
    if(str(n) == str(n)[::-1]):
        return(1)
    return(0)
toplam = 0
for i in range(1,1000000):
    if(ispalindrome(i) == 1 and ispalindrome(int(bin(i)[2:]))== 1):
        toplam += i
print(toplam)
