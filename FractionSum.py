class Fractions:
    def input_fractions(self):
        print("Enter no. of fractions to add")
        n = int(input())
        fractions = list()
        for i in range(n):
            print("Input fraction no. ", i+1, " separated by '/'");
            frac = [int(i) for i in input().split('/')];
            num = int(frac[0]);
            den = int(frac[1]);
            fractions.append(Fraction(num,den))
        return fractions

    def compute_sum_2_fracs(self, frac1, frac2):
        num_sum = 0
        den_prod = frac1.den*frac2.den
        num_sum = frac1.den*frac2.num + frac2.den*frac1.num

    def output_fractions(self, fractions):
        for i in range(len(fractions)):
            self.output_fraction(fractions[i])

    def output_fraction(self, Fraction):
        print(Fraction.num,"/",Fraction.den)

    def reduce(self, fraction):
        i = int(fraction.den/2)+1
        while i > 1:
            if ((fraction % i) == 0) and ((de


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
def main():
    obj = Fractions()
    fractions = obj.input_fractions()
    obj.output_fractions(fractions)

if __name__ == "__main__":
    main()
