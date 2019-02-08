class fibo:
	def __init__(self,n):
		self.n = n
		self.fib = 0
		self.b = 1
	def __iter__(self):
		while(self.n>self.fib):
			tmp = self.fib
			self.fib += self.b
			self.b = tmp
			yield tmp
n = 10
for i in fibo(n):
    print(i)
