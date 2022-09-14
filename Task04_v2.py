# Вариант 2
import random

k = int(input('Введите степень k: '))
result = f'{random.randint(-100, 101)}*x^{k}'
print(result, end='')
while k > 2:
    A = random.randint(-100, 101)
    if A > 0:
        result = f'+{A}*x^{k-1}'
        print(result, end='')
    elif A < 0:
        result = f'{A}*x^{k-1}'
        print(result, end='')
    k = k - 1
B = random.randint(-100, 101)
if B > 0:
    result = f'+{B}x'
    print(result, end='')
elif B < 0:
    result = f'{B}x'
    print(result, end='')
else:
    result = ''
    print(result, end='')
C = random.randint(-100, 101)
if C > 0:
    result = f'+{C}'
    print(result, end='')
elif C < 0:
    result = f'{C}'
    print(result, end='')
else:
    result = ''
    print(result, end='')
print('\n')
