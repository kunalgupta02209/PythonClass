class EgyptianFraction(object):
    """docstring for EgyptianFraction."""
    def __init__(self):
        super(EgyptianFraction, self).__init__()

    def input_testcase(self):
        elements = int(input())
        fractions = list()
        for i in range(elements):
            fractions.append(int(input()))
        self.compute(fractions, elements)

    def compute(self, fractions, elements):
        numerator = list()
        denominator = 1
        for i in range(elements):
            prod = 1
            for j in range(elements):
                if j != i:
                    prod = prod*fractions[j]
            numerator.append(prod)
            denominator = denominator*fractions[i]
        numSum = 0
        for i in range(elements):
            numSum = numSum + numerator[i]
        for i in range(elements):
            if (numSum % fractions[i]) == 0:
                numSum = numSum/fractions[i]
                denominator = denominator/fractions[i]
        fractions.sort()
        i = (fractions[elements-1])/2
        while i > 1:
            if ((numSum % i) == 0) and ((denominator % i) == 0):
                numSum = numSum/i
                denominator = denominator/i
            i = i - 1
        self.output(fractions, elements, numSum, denominator)

    def output(self, fractions, elements, numSum, denominator):
        for i in range(elements):
            if i != elements-1:
                print(f'1/{fractions[i]} + ', end='')
            else:
                print(f'1/{fractions[i]} =', end='')
        print(f"{numSum}/{denominator}")

print("Enter the no. of testcases")
testcases = int(input())
obj = EgyptianFraction()
for i in range(testcases):
    print("Input no. of fractions")
    obj.input_testcase();
