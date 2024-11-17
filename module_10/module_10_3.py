import threading
from random import randrange
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            tranc = randrange(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += tranc
            print(f'Пополнение: {tranc}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(1, 101):
            tranc = randrange(50, 500)
            print(f'Запрос на {tranc}')
            if self.balance >= 500 and self.lock.locked():
                self.balance -= tranc
                print(f'Снятие: {tranc}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
