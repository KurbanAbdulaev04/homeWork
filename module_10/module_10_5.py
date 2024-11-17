from multiprocessing import Process, Pool
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

files = [f'Files/file {i}.txt' for i in range(1, 5)]

# start_time = time()
# for i in files:
#     read_info(i)
# end_time = time()
# print(round(end_time-start_time, 2))

if __name__ == '__main__':
    start_t = time()
    with Pool() as pool:
        res = pool.map(read_info, files)
    end_t = time()
    print(round(end_t-start_t, 2))
