#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = int(input('Укажите размер списка: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
my_list = []
final_list = []

import random
for i in range(n):
    my_list.append(random.randint(min, max))
print(f'Исходный список: {my_list}')

for i in range(len(my_list)):
    if my_list.count(i)==1:
        final_list.append(i)
print(f'Список неповторяющихся элементов: {final_list}')