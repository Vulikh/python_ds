
from abc import ABC, abstractmethod

'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class DateError(Exception):
    pass

class Date:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def date_extratcion(cls, date):
        day, month, year = list(map(int, date.split('-')))
        return day, month, year

    @staticmethod
    def date_validation(date):
        day, month, year = list(map(int, date.split('-')))
        days_30 = [1, 3, 5, 7, 8, 10, 12]
        if year < 0:
            raise DateError('Wrong value for year')
        if month == 0 or month > 12:
            raise DateError('Wrong value for month')
        if day == 0 or day > 31 :
            raise DateError('Wrong value for day')
        if month in days_30 and day > 30:
            raise DateError(f'Wrong value for day in months {days_30}')
        elif month == 2 and day > 29:
            raise DateError('Wrong value for day in february')
        return True

first_date = Date('28-02-2018')
second_date = Date('28-13-0105')
third_date = Date('2019-00-28')

try:
    print(Date.date_validation(second_date.date))
except DateError:
    print('Wrong date')

date = Date.date_extratcion(first_date.date)
print(date)



'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
'''

class MineZeroDivisionError(Exception):
    pass



try:
    n, m = list(map(int, input('Enter two number to divide ').split()))
    if m == 0:
        raise MineZeroDivisionError
    print(n/m)
except MineZeroDivisionError:
    print('ZeroDivisionError')


'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

# Вариант №1

class OnlyNumbersError(Exception):
    pass

lst = []

while True:
    try:
        el = input('Enter a number, to stop type "stop"')
        if el.isdigit():
            lst.append(int(el))
        elif el == 'stop':
            break
        else:
            raise OnlyNumbersError
    except OnlyNumbersError:
        print('You can add only numbers')

print(*lst)

# Вариант №2

class MyList(list):
    def append(self, el):
        if el.isdigit():
            super().append(int(el))
        else:
            raise OnlyNumbersError

lst = MyList()

while True:
    try:
        el = input('Enter a number, to stop type "stop"')
        if el == 'stop':
            break
        lst.append(el)
    except OnlyNumbersError:
        print('You can add only numbers')

print(*lst)

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
'''

class StockError(Exception):
    pass


class Warehouse:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.stock = dict()

    def __str__(self):
        return f'Equipments at the warehouse {self.name} : {self.stock} '

    def check_capacity(self, *new_eq):
        if len(self.stock) + len(new_eq) > self.capacity:
            return False
        return True

    def take_to(self, *equipments):
        if self.check_capacity(equipments):
            for eq in equipments:
                if self.stock.get(eq.type):
                    self.stock[eq.type] += [eq]
                else:
                    self.stock[eq.type] = [eq]

    def take_out(self, subdivision, eq):
        try:
            if eq.type in self.stock:
                for s in self.stock[eq.type][:]:
                    if s.inv_num == eq.inv_num:
                        print(self.stock[eq.type])
                        subdivision.equipments.append(s)
                        print(f'Equipment {s.name} {s.inv_num} is transfered to the {subdivision.name}')
                        self.stock[eq.type].remove(s)
            else:
                raise StockError('Equipment not in the warehouse')
        except StockError as se:
            print(se)

    def num_of(self, type):
        try:
            return len(self[type])
        except KeyError:
            print(f'No {type} equipment at warehouse')

class Subdvision:

    def __init__(self, name):
        self.name = name
        self.equipments = []

    def __str__(self):
        return f'Equipments at the subdivision {self.name} : {self.equipments}'


class OfficeEquipment(ABC):

    def __init__(self, name, price, inv_num):
        self.name = name
        self.price = price
        self.inv_num = inv_num

    def __repr__(self):
        return f'{self.name} {self.price} {self.inv_num}'

    @property
    @abstractmethod
    def about(self):
        pass

class Monitor(OfficeEquipment):

    def __init__(self, name, price, inv_num, diag):
        super().__init__(name, price, inv_num)
        self.diag = diag
        self.type = 'Monitor'


    def about(self):
        return f'name : {self.name} diag : {self.diag}'


class Copier(OfficeEquipment):

    def __init__(self, name, price, inv_num, resolution):
        super().__init__(name, price, inv_num)
        self.type = 'Copier'
        self.resolution = resolution

    def about(self):
        return f'name : {self.name} resolution : {self.resolution}'


class Printer(OfficeEquipment):

    def __init__(self, name, price, inv_num, is_colored = False):
        super().__init__(name, price, inv_num)
        self.is_color = is_colored
        self.type = 'Printer'

    def about(self):
        return f'name : {self.name}  is color : {is_colored}'

def main():
    w = Warehouse('First warehouse', 50)
    sd = Subdvision('Subdivison 1')
    m = Monitor('first monitor', 3200, 'm5463aa', 19)
    m1 = Monitor('second monitor', 5600, 'm5464aa', 24)
    c = Copier('first copier', 1000, 'c3234dd', 566)
    c1 = Copier('second copier', 1100, 'c3235dd', 566)
    p = Printer('first printer', 500, 'p3314uu', True)
    p1 = Printer('second printer', 400, 'p3315uu', False)
    w.take_to(m, m1, c, c1, p, p1)
    print(w)
    w.take_out(sd, m1)
    print(sd)
    print(w)
main()





'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return f'{self.real} + {self.img}i' if self.img > 0 else f'{self.real} - {abs(self.img)}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img, self.real * other.img + other.real * self.img)


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(3, -1)

print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)
