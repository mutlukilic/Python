fifth = []
for n in range(10**3,354294):
    powers = 0
    for i in str(n):
        powers += int(i)**5
    if(powers == n):
        fifth.append(powers)
print(sum(fifth))
"""toplam = 0
for i in range(1000,354294):
    control = 0
    for j in str(i):
        control += int(j)**5
    if i == control:
        toplam += control
print(toplam)"""
        
