def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        for i in range(2, int(res/2 + 1)):
            if res % 1 == 0 and res % res == 0:
                print('Составное')
                return res
            else:
                print('Простое')
                return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    total = a + b + c
    return total


result = sum_three(3, 3, 3)
print(result)
