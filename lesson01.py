# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел 
# и строк и сохраните в переменные,выведите на экран.

a = 123
b = 4.2
c = 'abcdef'

print(a, b, c)

number1 = int(input('Введите число 1 '))
number2 = int(input('Введите число 2 '))
string1 = int(input('Введите строку 1'))
string2 = int(input('Введите строку 2'))

print(number1, number2, string1, string2)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
# Используйте форматирование строк.

sec = abs(int(input('Введите количество секунд')))
hours = (sec // 3600) % 24
minutes = (sec // 60 - hours * 60) % 60
seconds = (sec - minutes*60 - hours*3600) % (60*60*24)

print(f'{hours//10}{hours%10}:{minutes//10}{minutes%10}:{seconds//10}{seconds%10}')

# # 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input()
print(int(n) + int(2*n) + int(3*n))


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input('Введите число')))
div1 = 10
div2 = 1
max = 0
c = number

while c > 0:
	c //= div2
	if number % div1 // div2 > max:
		max = number % div1 // div2
	div1 *= 10
	div2 *= 10
	 

print(max)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом 
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
#  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
#  Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

a = input('Введите значения выручки и издержек через пробел ').split()

revenue = int(a[0])
costs = int(a[1])

if revenue > costs:
	print('Вы работаете в "+"')
	staff = int(input('Введите численность сотрудников '))
	rev_per_emp = (revenue - costs) / staff
	print(f'Прибыль в расчете на одного сотрудника составляет {rev_per_emp}')
elif revenue < costs:
	print('Вы работаете в "-"')
else:
	print('Вы работаете в 0')


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
#  на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения 
#  параметров a и b и выводить одно натуральное число — номер дня.


arr = input('Введите значения через пробел').split()
a = int(arr[0])
b = int(arr[1])

number_of_day = 1

while a < b:
	a *= 1.1
	number_of_day += 1

print(number_of_day)


