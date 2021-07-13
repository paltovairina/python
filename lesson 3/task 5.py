def sum_funk():
    """
    Возвращает сумму введенных чисел. При введении специального символа(#) работа программы завершается,
    при этом введенные до него числа прибавляются к полученной ранее сумме.
    :return:
    """
    res = 0
    while True:
        numbers = input("Введите строку чисел,разделенных пробелом, или #,чтобы завершить программу: ").split()
        for el in numbers:
            try:
                if el == "#":
                    print(f" Сумма чисел равна {res}. Программа завершена")
                    return
                else:
                    res += int(el)
            except ValueError:
                print("Можно вводить только числа или специальный символ!")
        print(f"Сумма чисел равна {res}")


print(sum_funk())
