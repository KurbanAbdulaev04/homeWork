class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # # до
    # def start(self):
    #     finishers = {}
    #     place = 1
    #     while self.participants:
    #         for participant in self.participants:
    #             participant.run()
    #             if participant.distance >= self.full_distance:
    #                 finishers[place] = participant
    #                 place += 1
    #                 self.participants.remove(participant)
    #
    #     return finishers

    # после...
    # если на не нужно отслеживать бегуна на этом расстоянии то,
    # вместо метода run, можно узнать время, за которое бегун пробежит данное расстояние,
    # можно также добавить метод (который рассчитывает это время) в классе Runner
    def start(self):
        finishers = {}
        place = 1
        # генерируем словарь у которого ключ=имя: значение=время
        dict_time = {i.name: self.full_distance/i.speed for i in self.participants}
        # сортируем этот словарь, который будет списком с картежами
        sorted_list_on_time = sorted(dict_time.items(), key=lambda item: item[1])
        for i in sorted_list_on_time:
            finishers[place] = i[0]
            place += 1

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())