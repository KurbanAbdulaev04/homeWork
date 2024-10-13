immutable_var = (True, 2, "commit", 5.3)
print(immutable_var)

# immutable_var[1] = 5
# выдаст ошику т. к.
# кортеж сам по себе неизменяем, но если он содержит изменяемые объекты,
# можем менять содержимое этих объектов

mutable_list = [0, False, "String", 6.3]
mutable_list[0] = 1
print(mutable_list)