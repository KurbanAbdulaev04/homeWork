my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0

while count < len(my_list):
    if my_list[count] > 0:
        print(my_list[count])
        count += 1
    elif my_list[count] == 0:
        count += 1
    elif my_list[count] < 0:
        count += 1



# # так кажется будет поинтереснее
# for i in range(len(my_list)):
#     if my_list[i] > 0:
#         print(my_list[i])
#
# # или так
# one_list = [my_list[i] for i in range(len(my_list)) if my_list[i] > 0]
# print(one_list)