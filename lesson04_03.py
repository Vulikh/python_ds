from sys import argv
from itertools import count, cycle


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


number = int(argv[1])
array = argv[2]

for i in count(number):
	if i > 30:
		break
	print(i)

a = cycle(array)
el_counter = 3 * len(array)

while el_counter > 0:
	print(next(a))
	el_counter -= 1


