from itertools import cycle

c = 0
my_list = ["one", "two", "three", "four", "five"]
for el in cycle(my_list):
    if c >= 20:
        break
    else:
        print(el)
        c += 1
