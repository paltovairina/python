from itertools import count
from math import factorial


def factorial_generator():
    for i in count(1):
        yield factorial(i)


g = factorial_generator()
print(g)

n = 0
for el in g:
    if n < 5:
        print(el)
        n += 1
    else:
        break
