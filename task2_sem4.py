#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число N: '))
my_list = []
for i in range(1, N+1):
    if(N%i==0):
        my_list.append(i)
print(my_list)