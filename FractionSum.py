class Fractions:
    def input_fractions(self):
        print("Enter no. of fractions to add")
        n = int(input())
        numerator = list()
        denominator = list()
        for i in range(n):
            print("Input fraction no. ", i+1, " separated by '/'");
            frac = [int(i) for i in input().split('/')];
            numerator.append(int(frac[0]));
            denominator.append(int(frac[1]));
        fractions = dict()
        fractions["num"] = numerator
        fractions["den"] = denominator
        return fractions

    def compute(self, fractions):
        num = fractions["num"]
        den = fractions["den"]
    def output_fractions(self, fractions):
        num = fractions["num"]
        den = fractions["den"]
        for i in range(len(num)):
            self.output_fraction(num[i],den[i])
    def output_fraction(self, num, den):
        print(num,"/",den)

def main():
    obj = Fractions()
    fractions = obj.input_fractions()
    obj.output_fractions(fractions)

if __name__ == "__main__":
    main()
