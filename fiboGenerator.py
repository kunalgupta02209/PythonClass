def fib(n):
	fib =0
	b = 1
	while(fib < n):
		yield fib
		fib, b = fib +b,fib
n = 30
for i in fib(n):
    print(i)
