import time
start_time = time.time()
fibonacci,i = [1,1],0
while(True):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
    if(fibonacci[i+2]/(10**999) == 1):
        break
    i += 1
print(fibonacci.index(fibonacci[i+2])+1)
"""a,b,n = 1,1,2
while len(str(b)) < 1000:
    a,b,n = b,a+b,n+1
print(n)"""
print(time.time()-start_time,"seconds")

