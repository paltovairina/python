new_str = input("Введите предложение из нескольких слов,разделенных только пробелами:")
new_list = new_str.split()
print(new_list)
for ind, el in enumerate(new_list):
    if len(el) > 10:
        el = el[0:10]
    print(f"{ind + 1}.{el}")
