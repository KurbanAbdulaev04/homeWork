from time import sleep


class User:
    '''
    Класс пользователя, содержащий атрибуты: имя пользователя, пароль, возраст
    '''
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title:str, duration:int, time_now=0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube:
    def __init__(self):
        self.users =[]
        self.videos = []
        self.current_user = None

    def register(self, nickname:str, password:str, age:int):
        self.password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname:str, password:str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word:str):
        list_videos = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                list_videos.append(i.title)
        return list_videos

    def watch_video(self, movie):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in self.videos:
            if i.title == movie:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for j in range(1, 11):
                    print(j, end='')
                    sleep(1)
                    i.time_now += 1
                i.time_now = 0
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
