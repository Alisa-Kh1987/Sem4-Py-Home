#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#1ый вариант восприятия условия задачи (когда в конечном списке остаются числа, встречающиеся в исходной последовательности только 1 раз)
# n = int(input('Укажите размер списка: '))
# min = int(input('Введите минимальное значение диапазона: '))
# max = int(input('Введите максимальное значение диапазона: '))
# my_list = []
# occurrences = []
# final_list = []

# import random
# for i in range(n):
#     my_list.append(random.randint(min, max))
# print(f'Исходный список: {my_list}')

# for item in my_list :
#     count = 0
#     for x in my_list :
#         if x == item :
#             count += 1
#     occurrences.append(count)
# final_list = set()
# index = 0
# while index < len(my_list) :
#     if occurrences[index] == 1 :
#         final_list.add(my_list[index])
#     index += 1
# print(final_list)

#2-й вариант восприятия условия задачи (когда из исходного списка убираются все дубликаты, оставляя в конечном списке по 1 вхождению каждого числа исходного списка)

n = int(input('Укажите размер списка: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
my_list = []
final_list = []

import random
for i in range(n):
    my_list.append(random.randint(min, max))
print(f'Исходный список: {my_list}')

for number in my_list:
        if number in final_list:
            continue
        else:
            final_list.append(number)
print(final_list)