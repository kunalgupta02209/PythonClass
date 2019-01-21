class Split:
	def inputString(self):
		return input()
	#def inputEquation(self):
	#	return input()
	def convertToLOT(self, string):
		l = string.split(";")
		li= list()
		for x in l:
			tup = tuple(x.split('='))
			li.append(tup)
		return li
	def printLOT(self, li):
		print(li)

def main():
	#string = "a=b;c=d;e=f"
	obj = Split()
	print("Enter the string")
	string = obj.inputString()
	li = obj.convertToLOT(string)
	obj.printLOT(li)

if __name__ == "__main__":
	main()
