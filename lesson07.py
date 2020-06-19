from abc import ABC, abstractmethod

"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

"""


class MatrixAddError(Exception):
    pass


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def check_matrix(self, other):
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    return False
        else:
            return False
        return True

    def __str__(self):
        string = '\n'.join([' '.join([str(j) for j in row]) for row in self.matrix])
        return string

    def __add__(self, other):
        if self.check_matrix(other):
            result = []
            for i in range(len(self.matrix)):
                result.append([self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))])
            return Matrix(result)
        else:
            raise MatrixAddError


a = Matrix([[1, 2], [4, 5], [7, 8]])
b = Matrix([[1, 2], [4, 5], [7, 8]])

print(a)

try:
    print(a + b)
except MatrixAddError:
    print("Enter 2 matrix with same number of row and column")

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора
@property.
"""


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        return self.size


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5 , 2)


class Costume(Clothes):
    @property
    def consumption(self):
        return 2 * self.size + 0.3


coat = Coat(5)
costume = Costume(7)

print(coat.consumption)
print(costume.consumption)


"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
 вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны 
 применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) 
 деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме 
ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток 
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек 
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
 Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n*****.
"""

class Cell:

    def __init__(self, size):
        self.size = int(size)

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        if self.size >= other.size:
            return self.size - other.size
        return other.size - self.size

    def __mul__(self, other):
        return self.size * other.size

    def __truediv__(self, other):
        if self.size // other.size > 0:
            return self.size // other.size
        return other.size // self.size

    def make_order(self, count):
        if count < self.size:
            p = self.size // count
            o = self.size % count
            result = ''
            for i in range(p):
                for j in range(count):
                    result += '* '
                result += '\n'
            result += "* " * o
        else:
            result = '* ' * self.size
        return result


cell1 = Cell(12)
cell2 = Cell(20)

print(cell1 + cell2)
print(cell1 / cell2)
print(cell1 * cell2)
print(cell1 - cell2)
print(cell1.make_order(12))
