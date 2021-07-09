seasons_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
                9: "autumn", 10: "autumn", 11: "autumn", 12: "winter}"}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
while month < 1 or month > 12:
    print("Неверно задан номер месяца")
    month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
print(seasons_dict.get(month))

