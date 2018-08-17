class EgyptianFraction(object):
    """docstring for EgyptianFraction."""
    def __init__(self):
        super(EgyptianFraction, self).__init__()

    def input_testcase(self):
        elements = int(input())
        fractions = list()
        for i in range(elements):
            fractions.append(int(input()))
        compute(fractions, elements)

    def compute(self, fractions, elements):
        numerator = list()
        denominator = 1
        for i in range(elements):
            prod = 1;
            j = i+1
            while (j != i):
                j = j%elements
                prod = prod*fractions[j]
                j++
            numerator.append(prod)
            denominator = denominator*fractions[i]
        numSum = 0
        for i in range(elements):
            numSum = numSum + numerator[i]
        for i in range(elements):
            if (numSum % fractions[i]) == 0:
                numSum =

print("Enter the no. of testcases")
testcases = int(input())
obj = EgyptianFraction()
for i in range(testcases):
    print("Input no. of fractions")
    obj.input_testcase();
