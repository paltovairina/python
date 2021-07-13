def my_func(arg_1, arg_2, arg_3):
    """
    Возвращает сумму наибольших двух аргументов из трех введённых
    :param arg_1: float
    :param arg_2: float
    :param arg_3: float
    :return: сумма наибольших двух аргументов
    """
    sum_max = arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    return sum_max


print(my_func(float(input("Введите число №1: ")), float(input("Введите число №2: ")),
      float(input("Введите число №3: "))))
