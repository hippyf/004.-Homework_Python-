# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

N = int(input('Введите количество чисел в последовательности: '))
chisla = []
for i in range (N):
    chisla.append(input(f'Введите {i+1} - e число: '))

print(f'Список неповторяющихся элементов {set(chisla)}')

