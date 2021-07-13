def division_func():
    """
    Возвращает результат деления чисел
    :param divd:dividend,делимое,type float
    :param divs: divisor,делитель, type float
    :return: quatient, результат деления, type float
    """
    while True:
        try:
            divd = float(input("Введите делимое: "))
            divs = float(input("Введите делитель: "))
            quat = divd / divs
            break
        except ZeroDivisionError:
            print("Нельзя делить на ноль!")
        except ValueError:
            print("Вы ввели не числа!")
    return quat


print(f"Результат деления = {division_func()}")
