from threading import Thread
from time import sleep, time

def write_words(word_count: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as file:
        print(f'Началась запись в файл {file_name}')
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}\n')


start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = round(time(), 2)
print(f'Время работы функции в однопоточном режиме: {round(end_time - start_time, 2)}\n')

start_time2 = time()

flow1 = Thread(target=write_words, args=(10, 'example5.txt'))
flow2 = Thread(target=write_words, args=(30, 'example6.txt'))
flow3 = Thread(target=write_words, args=(200, 'example7.txt'))
flow4 = Thread(target=write_words, args=(100, 'example8.txt'))

flow1.start()
flow2.start()
flow3.start()
flow4.start()
flow1.join()
flow2.join()
flow3.join()
flow4.join()

end_time2 = time()
print(f'Время работы в многопоточном режиме: {round(end_time2-start_time2, 2)}')