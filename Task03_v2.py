# Вариант 2

N = int(input('Введите количество чисел в последовательности: '))
chisla = []
for i in range (N):
    chisla.append(input(f'Введите {i+1} - e число: '))

spisok = []
for i in chisla:
    if i not in spisok:
        spisok.append(i)
print(f'Список неповторяющихся элементов: {spisok}')
