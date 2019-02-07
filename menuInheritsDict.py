class menu:
	def __init__(self):
		self.itemDict= {}
	def __setitem__(self,item,value):
		self.itemDict[item] = value
	def __getitem__(self,item):
		#print(type(item))
		#item = next(iter(self.itemDict))
		return self.itemDict[item]
	def __contains__(self,item):
		print("Called contains")
		if(item in self.itemDict):
			return item
		else:
			return ""
	def __iter__(self):
		return iter(self.itemDict)

def main():
	m=menu()
	m["idly"] = 10
	m["vada"] = 20
	#print(type(m))
	if "idly" in m:
		print("abc","idly" in m)
		for i in m:
			#print(i)
			print(i,m[i])

if __name__ == '__main__':
	main()
