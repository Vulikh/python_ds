from time import sleep

"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод 
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: 
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 
2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в 
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


class TrafficLight:

    def __init__(self):
        self._color = 'red'
        print("Red")

    def running(self):
        sleep(7)
        self._color = 'yellow'
        print("Yellow")
        sleep(2)
        self._color = 'green'
        print("Green")
        sleep(9)


tl = TrafficLight()
tl.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого 
для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта 
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def calculate_mass(self):
        return self._length * self._width * 15 * 5


r = Road(100, 100)
print(r)
print(r.calculate_mass())

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут должен быть 
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name,  self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position("Michael", "Scott", "Regional manager", 10000, 2000)

print(p.get_full_name())
print(p.get_total_income())


"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость 
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.direction = ''

    def go(self):
        print("Car is running")

    def stop(self):
        self.speed = 0
        print("Car is stopped")

    def turn(self, direction):
        self.direction = direction
        print(f"Car is going to {self.direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Speed warning")
        super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):

    def turn_on_flasher(self):
        self.flasher_on = True
        print('Flasher is ON')

    def turn_on_flasher(self):
        self.flasher_on = False
        print('Flasher if OFF')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Speed warning")
        super().show_speed()


pc = PoliceCar(60, 'green', 'Police car', True)
sc = SportCar(150, 'green', 'Sport car', True)
wc = WorkCar(60, 'green', 'Work car', True)
tc = TownCar(70, 'green', 'Town car', True)

cars = [pc, sc, wc, tc]
for car in cars:
    print(car.name)
    car.show_speed()
    car.go()
    car.turn('left')
    car.stop()
    if car is pc:
        car.turn_on_flasher()

'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
'''


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):

    def draw(self):
        print(f'Pen "{self.title}" is started to draw')


class Pencil(Stationery):

    def draw(self):
        print(f'Pencil "{self.title}" is started to draw')


class Handle(Stationery):

    def draw(self):
        print(f'Handle "{self.title}" is started to draw')


pen = Pen('Pen_1')
pencil = Pencil('Pencil_1')
handle = Handle('Hangle_1')

stationeries = [pen, pencil, handle]

for st in stationeries:
    st.draw()

