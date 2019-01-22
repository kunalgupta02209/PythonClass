def inputString():
	return input()
#def inputEquation(self):
#	return input()
def convertToLOT(string):
	lis = [tuple(i.split('=')) for i in string.split(';')];
	return lis

def printLOT(li):
	print(li)

def main():
	#string = "a=b;c=d;e=f"
	print("Enter the string")
	string = inputString()
	li = convertToLOT(string)
	printLOT(li)

if __name__ == "__main__":
	main()
