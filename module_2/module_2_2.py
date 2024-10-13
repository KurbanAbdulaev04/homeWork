first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)



# # введение чисел и присвоение их переменным
# # используем try-except, чтобы не выходила ошибка, если не ввели какое-либо число
# try:
#     first = int(input('Первое число: '))
# except ValueError:
#     print('Первое число не введено!')
# try:
#     second = int(input('Второе число: '))
# except ValueError:
#     print('Второе число не введено!')
# try:
#     third = int(input('Третье число: '))
# except ValueError:
#     print('Третье число не введено!')
#
# # пишем условную конструкцию, которая выводит кол-во одинаковых чисел среди 3-х введённых
# # также используем try-except, чтобы не выходила ошибка, если не ввели одно или несколько чисел
# try:
#     if first == second == third:
#         print(3)
#     elif first == second or first == third or second == third:
#         print(2)
#     else:
#         print(0)
# except NameError:
#     print('Некоторые чисела не введены!')