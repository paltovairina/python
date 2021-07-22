rus_numb_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
f = open("numbers.txt", "r")
rus_f = open("rus_numbers.txt", "w", encoding="UTF-8")
numbers_eng = f.read().split("\n")
for line in numbers_eng:
    numb = line.split()
    print(line.replace(numb[0], rus_numb_dict.get(numb[0])), file=rus_f)
f.close()
rus_f.close()