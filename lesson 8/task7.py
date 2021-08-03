class ComplexNumbers:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex_number = complex(a, b)

    def __add__(self, other):
        return f"Cумма комплексных чисел равна: z = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"Произведение комплексных чисел равно: " \
               f"z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"


cn_1 = ComplexNumbers(1, 2)
print(cn_1.complex_number)
cn_2 = ComplexNumbers(3, 4)
print(cn_1 + cn_2)
print(cn_1 * cn_2)
