fib=[]
for i in range(0,20):
    if i==0:
        fib.append(0)
    elif i==1:
        fib.append(1)
    else:    
        fib.append(fib[i-2]+fib[i-1])

print(fib)
