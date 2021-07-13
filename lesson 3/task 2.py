def person_inform():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    year = int(input("Введите год вашего рождения: "))
    city = input("Введите город проживания: ")
    email = input("Введите ваш email: ")
    telephone = input("Введите номер вашего телефона: ")
    print(f"Имя - {name}, фамилия - {surname}, год рождения - {year}, город проживания - {city}, email - {email},"
          f" номер телефона - {telephone}")


print(person_inform(), end='')
