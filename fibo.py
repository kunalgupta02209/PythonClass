class fibo:
	def __init__(self,n):
		self.ar = []
		self.genFib(n)
	def __contains__(self,i):
		return i in self.ar
	def __iter__(self):
		return iter(self.ar)
	def genFib(self,n):
		self.ar.extend([0,1])
		while(self.ar[-1] <= n):
			self.ar.append(self.ar[-2]+self.ar[-1])
n = 10
for i in fibo(n):
    print(i)
