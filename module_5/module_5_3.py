# создаем класс
class House:
    # создаем метод __init__, и передаем в нее аргументы (name, number_of_floors)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # создаем метод go_to, и передаем в нее аргумент (new_floor)
    def go_to(self, new_floor):
        # чтобы числа шли в столбик, перебираем в цикле
        for i in range(1, new_floor + 1):  # +1 т.к. последнее число не берется
            # в цикле создаем условие
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                # что-бы цикл не продолжал перебирать используем break
                break
            else:
                print(i)

    # создаем метод, который возвращает количество этажей
    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

        # не уверен что есть нецельное число(число с плавающей точкой(float)) этажей
        # и на строки не знаю надоли проверять (в условии задачи не сказано)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >+ other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    # и метод, который будет вовращать строку "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
