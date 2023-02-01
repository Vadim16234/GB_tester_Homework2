# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0


import random

n = int(input('Введите количество монеток: '))
m = []
for num in range(0,n):
    random_number = round(random.uniform(0,1))
    m.append(random_number)

print(n)
print(m)

count = 0
orel = 0
reshka = 0
for item in m:
    if item > 0:
        orel = orel + 1
    elif item in m:
        if item == 0:
            reshka = reshka + 1
if orel < reshka:
    print('Необходимо перевернуть', orel, 'монеток')
else:
    print('Необходимо перевернуть', reshka, 'монеток')