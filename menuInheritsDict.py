class menu(dict):
	def __init__(self):
		self.itemDict= {}
def main():
	m=menu()
	m["idly"] = 10
	m["vada"] = 20
	if "idly" in m:
		for i in m:
			print(i,m[i])

if __name__ == '__main__':
	main()
