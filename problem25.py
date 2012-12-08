fib = [1,1]
i=1
while len(str(fib[i])) != 1000:
	i+=1
	fib.append(fib[i-1]+fib[i-2])
print i+1, fib[i]