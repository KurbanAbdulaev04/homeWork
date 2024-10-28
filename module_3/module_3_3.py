def print_params(a=1, b='строка', c=True):
    print((a, b, c))

print_params(4, 'hello', 5)
print_params(False, True, False)
print_params()

print()
print_params(b = 25)
print_params(c = [1,2,3])

print()
values_list = ['World', 10, True]
values_dict = {'a': 2, 'b': 1, 'c': 0}
print_params(*values_list)
print_params(**values_dict)

print()
values_list_2 = [2.94, 'x']
print_params(*values_list_2, 42)