n = int(input("Введите число:"))
a = str(n) #переводим число в строку
b = a + a #объединяем строки
c = a + a + a
s = n + int(b) + int(c)
print(f"{n}+{int(b)}+{int(c)}={s}")
print(f"Ответ: {s}")



