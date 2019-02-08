class fibo:
	def __init__(self,n):
		self.n = n
		self.fib = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		if(self.fib > self.n):
			raise StopIteration
		else:
			tmp = self.fib
			self.fib = self.fib+self.b
			self.b = tmp
			return tmp
n = 10
for i in fibo(n):
    print(i)
