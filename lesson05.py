
from googletrans import Translator
from random import randint
from re import findall
import json

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open("new_file.txt", "w") as new_file:
	while True:
		line = input()
		if line:
			new_file.writelines(line + '\n')
		else:
			break


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("new_file.txt") as new_file:
	lines = []
	for line in new_file:
		lines.append(line.split())

for i, j in enumerate(lines, 1):
	print(f"line {i} with {len(j)} words")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.



with open("employees.txt") as emp:
	salaries = []
	print("Employees with salary below 20000:")
	for line in emp:
		employee, salary = line.replace(":", " ").split()
		if int(salary) < 20000 :
			print(employee)
		salaries.append(int(salary))
	print(f'Average salary : {sum(salaries)/len(salaries):.2f}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен 
# записываться в новый текстовый файл.


with open('numbers.txt') as num:
	translator = Translator()
	for line in num:
		w = line.split()
		with open('rus_nums.txt', 'a') as ru_n:
			w[0] = translator.translate(w[0], dest='ru').text
			ru_n.write(" ".join(w) + '\n')


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее 
# на экран.

with open("numbers_and_sum.txt", "w") as nas:
	result = 0
	for i in range(20):
		num = randint(0, 100)
		nas.write(str(num) + " ")
		result += num
	print(f'Sum of numbers in {nas.name} = {result}') 





# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому 
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все 
# типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий 
# по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —



with open("subjects.txt", encoding = 'utf-8') as sub:
	sub_dict = dict()
	for line in sub:
		subject, hours = line.split(":")
		hours = [findall(r"\d+", j) for j in hours.split()]
		int_hours = [int(y) for x in hours for y in x]
		sub_dict[subject] = sum(int_hours)

print(sub_dict)




# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать 
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также 
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


with open('firms.txt') as firms:
	list_firms = [dict(), {"average_profit" : 0}]
	average_profit = []
	for line in firms:
		name, form, profit, loss = line.split()
		profit, loss = int(profit), int(loss)
		result = profit - loss
		if result >= 0:
			average_profit.append(result)
		list_firms[0][name] = result
	list_firms[1]["average_profit"] = sum(average_profit)/len(average_profit)
	print(list_firms)
	with open('firms.json', "w") as json_firms:
		json.dump(list_firms, json_firms)


# Подсказка: использовать менеджеры контекста.