def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        if res % 2 == 0:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    total = a + b + c
    return total


result = sum_three(2, 3, 6)
print(result)
