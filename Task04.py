# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

A = random.randint(0, 101)
B = random.randint(0, 101)
C = random.randint(0, 101)
k = int(input('Введите степень k: '))
with open ('Task04.txt', 'w') as data:
    data.write(f'{A}*(x^{k}) + {B}*x + {C} = 0')