import time
start_time = time.time()
power = set()
for i in range(2,101):
    for j in range(2,101):
        power.add(i**j)
power = list(power)
power.sort()
print(len(power))

"""###Necdet Hoca
powers = []

for a in range(2,101):
    for b in range(2,101):
        powers.append(a**b)

powers.sort()

for n in powers:
    while powers.count(n) > 1:
        powers.remove(n)

print(len(powers))"""

print time.time() - start_time,"seconds"
