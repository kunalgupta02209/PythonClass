class EgyptianFraction(object):
    """docstring for EgyptianFraction."""
    def __init__(self):
        super(EgyptianFraction, self).__init__()

    def input_testcase(self):
        elements = int(input())
        fractions = list();
        for i in range(elements):
            fractions.append(int(input()))
            



print("Enter the no. of testcases")
testcases = int(input())
obj = EgyptianFraction()
for i in range(testcases):
    print("Input no. of fractions")
    obj.input_testcase();
