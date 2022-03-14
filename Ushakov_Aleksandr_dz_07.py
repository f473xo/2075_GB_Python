class ComplexNumber:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self,):
        return f'{self.a + self.b}'


num1 = ComplexNumber(1, 3j)
num2 = ComplexNumber(3, 7j)
print(num1 + num2)
print(num1 * num2)
