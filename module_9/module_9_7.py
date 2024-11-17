from random import randrange


def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        for i in range(2, int(res/2 + 1)):
            if res % i == 0:
                print(f'Составное')
                return res
        print(f'Простое')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    total = a + b + c
    return total


result = sum_three(randrange(3, 10), randrange(3, 10), randrange(3, 10))
print(result)
