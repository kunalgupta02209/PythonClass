class Menu:
	def __init__(self):
		self.itemDic={}
	def add(self, item, price):
		self.itemDic[item] = price
	def remove(self, item):
		self.itemDic.pop(item)
	def show(self):
		for k,v in self.itemDic.items():
			print(k," = ",v)
		#print(self.itemDic.items())


def main():
	m=Menu()
	b = Menu()
	m.add("idly",10)
	m.add("vada",20)
	m.show()
	b.show()
	m.remove("idly")
	m.show()

if __name__ == "__main__":
	main()
