with open("numbers_f.txt", 'w+') as numb_f:
    numbers = input("Введите цифры через пробел: ")
    numb_f.writelines(numbers)
    single_numb = numbers.split()
    int_numb = [int(x) for x in single_numb]
    sum_numb = sum(int_numb)
    print(sum_numb)
