# создаем класс
class House:
    # создаем метод __init__, и передаем в нее аргументы (name, number_of_floors)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # создаем метод go_to, и передаем в нее аргумент (new_floor)
    def go_to(self, new_floor):
        # чтобы числа шли в столбик, перебираем в цикле
        for i in range(1, new_floor + 1): # +1 т.к. последнее число не берется
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

    # и метод, который будет вовращать строку "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))