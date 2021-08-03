class OwnErrorNumberInList(Exception):
    def __init__(self, txt):
        self.txt = txt


numbers_list = []
yes_no_input = input("Вы хотите добавить число в список?Yes/no: ")
while yes_no_input == "Yes":
    try:
        number_to_append = int(input("Введите число для добавления в список: "))
        numbers_list.append(number_to_append)
        yes_no_input = input("Вы хотите добавить число в список?Yes/no: ")

        if type(number_to_append) != int:
            raise OwnErrorNumberInList("Вы ввели не число!")
    except OwnErrorNumberInList as err:
        print(err)
        number_to_append = input("Введите число для добавления в список:")
    except ValueError:
        print("Вы ввели не число!")

if yes_no_input == "No":
    print(numbers_list)
