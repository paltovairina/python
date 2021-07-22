f = open("new_file.txt", "w")
while True:
    string_file = input("Введите данные для записи в файл или пробел для завершения записи: ")
    if string_file == " ":
        print("Запись завершена.")
        break
    else:
        f.write(string_file + "\n")
f.close()
