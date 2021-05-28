#Предоставлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [433, 8, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')