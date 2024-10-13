my_dict = {'Ivan': 25, 'Maks': 27, 'Joe': 30}

print(my_dict)
print(my_dict['Ivan'])

print(my_dict.get('Denis'))

my_dict.update({'Egor': 25, 'Alexandr': 28})

a = my_dict.pop('Joe')
print(a)
print(my_dict)


my_set = {2, 7, 2, 3, True, 'str', True}
print(my_set)

my_set.update([4, 5])
# my_set.add(4)
# my_set.add(5)

my_set.discard(2)

print(my_set)