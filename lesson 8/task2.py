class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    input_dividend = int(input("Введите делимое: "))
except ValueError:
    print("Вы ввели не число!")
    input_dividend = int(input("Введите делимое: "))

try:
    input_divisor = int(input("Введите делитель:"))

    if input_divisor == 0:
        raise OwnZeroDivisionError("Делить на ноль нельзя!")
except OwnZeroDivisionError as err:
    print(err)
    input_divisor = int(input("Введите делитель:"))

except ValueError:
    print("Вы ввели не число!")
    input_divisor = int(input("Введите делитель:"))

result = input_dividend / input_divisor
print(result)
