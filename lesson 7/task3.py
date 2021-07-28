class Cell:
    def __init__(self, cell_number):
        self.cell_number = int(cell_number)

    def __add__(self, other):
        return f"Произошло объединение двух клеток. " \
               f"Число ячеек общей клетки равно {self.cell_number + other.cell_number}"

    def __sub__(self, other):
        sub = self.cell_number - other.cell_number
        if sub > 0:
            return f"Произошло уменьшение(вычитание) клеток." \
                   f"Число ячеек новой клетки равно {sub}"
        else:
            return f"Вычитание клеток невозможно"

    def __mul__(self, other):
        return f"Создается общая клетка из двух(умножение). " \
               f"Число ячеек общей клетки равно {self.cell_number * other.cell_number}"

    def __truediv__(self, other):
        return f"Создается общая клетка из двух(деление)." \
               f"Число ячеек общей клетки равно {self.cell_number // other.cell_number}"

    def make_order(self, line):
        result = ''
        for i in range(int(self.cell_number / line)):
            result += '*' * line + '\n'
        result += '*' * (self.cell_number % line) + '\n'
        return result


cell = Cell(40)
cell_2 = Cell(50)
print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell.make_order(5))

cell = Cell(87)
cell_2 = Cell(50)
print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell.make_order(10))

