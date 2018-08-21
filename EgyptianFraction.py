class EgyptianFraction:
    def input_testcase(self):
        elements = int(input())
        fractions = list()
        for i in range(elements):
            fractions.append(int(input()))
        return fractions


    def compute(self, fractions):
        numerator = list()
        denominator = 1
        for i in range(len(fractions)):
            prod = 1
            for j in range(len(fractions)):
                if j != i:
                    prod = prod*fractions[j]
            numerator.append(prod)
            denominator = denominator*fractions[i]
        numSum = 0
        for i in range(len(fractions)):
            numSum = numSum + numerator[i]
        print(numSum)
        for i in range(len(fractions)):
            print(numSum%fractions[i] == 0)
            if (numSum % fractions[i]) == 0:
                numSum = numSum/fractions[i]
                denominator = denominator/fractions[i]
        self.output(fractions, numSum, denominator)
        fractions.sort()
        print(fractions)
        i = (fractions[len(fractions)-1])
        while i > 1:
            if ((numSum % i) == 0) and ((denominator % i) == 0):
                numSum = numSum/i
                denominator = denominator/i
            i = i - 1
        return(numSum, denominator)

    def output(self, fractions, numSum, denominator):
        for i in range(len(fractions)):
            if i != len(fractions)-1:
                print(f'1/{fractions[i]} + ', end='')
            else:
                print(f'1/{fractions[i]} =', end='')
        print(f"{numSum}/{denominator}")

def main():
    print("Enter the no. of testcases")
    testcases = int(input())
    obj = EgyptianFraction()
    list_of_testcases = list()
    numSum = list()
    denom = list()
    for i in range(testcases):
        print("Input no. of fractions")
        list_of_testcases.append(obj.input_testcase());
        (n, d) = obj.compute(list_of_testcases[i])
        numSum.append(n)
        denom.append(d)

    for i in range(testcases):
        obj.output(list_of_testcases[i], numSum[i], denom[i])

if __name__ == "__main__":
    main()
