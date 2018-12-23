def gcd(num1, num2):
    while num1 % num2 != 0:
        old_num1 = num1
        old_num2 = num2

        num1 = old_num2
        num2 = old_num1 % old_num2
    return num2


class Fraction:
    def __init__(self, numerator, denominator) -> None:
        if str(numerator).isdigit() and str(denominator).isdigit():
            divisor = gcd(numerator, denominator)
            self.num = numerator // divisor
            self.den = denominator // divisor
        else:
            raise Exception('Numerator and Denominator should be int')

    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = (self.num * other.den) - (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num/self.den > other.num/other.den

    def __ge__(self, other):
        return self.num/self.den >= other.num/other.den

    def __lt__(self, other):
        return self.num/self.den < other.num/other.den

    def __le__(self, other):
        return self.num/self.den <= other.num/other.den

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __str__(self) -> str:
        return str(self.num) + '/' + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


f1 = Fraction(2, 3)
f2 = Fraction(2, 3)
print(f1.get_num())
print(f1.get_den())
print(f1 == f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(Fraction(1, 2) / Fraction(2, 1))
f4 = Fraction(1, 'b')
