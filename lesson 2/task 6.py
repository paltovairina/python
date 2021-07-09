goods = []
while input("Вы хотите добавить товар? (да/нет): ") == 'да':
    number = int(input("Введите номер товара: "))
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit_of_measure = input("Введите единицы измерения количества товара: ")
    features = {"название": name, "цена": price, "количество": quantity, "ед": unit_of_measure}
    goods.append(tuple([number, features]))
print(goods)
analytics = {}
for good in goods:
    for key, value in good[-1].items():
        if key in analytics:
            if value not in analytics.get(key):
                analytics.get(key).append(value)
        else:
            analytics.update({key: [value]})
print(f"Аналитика:{analytics}")
