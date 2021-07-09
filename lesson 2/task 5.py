my_list = [13, 8, 5, 5, 1]
new_number = int(input("Введите натуральное число:"))
count = my_list.count(new_number)
for el in my_list:
    if count > 0:
        ind = my_list.index(new_number)
        my_list.insert(ind + 1, new_number)
        break
    else:
        if new_number > el:
            ind_2 = my_list.index(el)
            my_list.insert(ind_2, new_number)
            break
        elif new_number < my_list[len(my_list) - 1]:
            my_list.append(new_number)
print(my_list)
