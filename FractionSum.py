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
        frac = Fraction(num_sum,den_prod)
        frac = self.reduce(frac)
        return frac

    def compute_sum_fracs_list(self, fractions):
        i = 0;
        n = len(fractions)
        while i < n:
            if(i == 0):
                frac = self.compute_sum_2_fracs(fractions[i], fractions[i+1])
                i += 2
            else:
                frac = self.compute_sum_2_fracs(frac, fractions[i])
                i += 1
        return frac

    def output_fractions(self, fractions):
        for i in range(len(fractions)):
            self.output_fraction(fractions[i])

    def output_fraction(self, Fraction):
        print(Fraction.num,"/",Fraction.den)

    def reduce(self, fraction):
        i = int(fraction.den/2)+2
        if fraction.num == fraction.den:
            fraction.num = 1
            fraction.den = 1
            return fraction
        while i > 1:
            if ((fraction.num % i) == 0) and ((fraction.den % i) == 0):
                fraction.num = int(fraction.num / i)
                fraction.den = int(fraction.den / i)
            i -= 1
        return fraction


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
def main():
    obj = Fractions()
    fractions = obj.input_fractions()
    fraction = obj.compute_sum_fracs_list(fractions)
    obj.output_fraction(fraction)

if __name__ == "__main__":
    main()
