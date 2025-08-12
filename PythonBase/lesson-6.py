# Псевдослучайные числа

import random

# randint() - функция, которая генерирует число на заданном интервале
# возвращает одно число типа int
num1 = random.randint(1, 10)
print(num1)

# random() - функция, которая генерирует число от 0 до 1
# возвращает одно число типа float
num2 = random.random()
print(num2)

# choice() - функция, которая выбирает один случайный элемент из списка
num3 = random.choice([1, 9, 'hello', 74, {'name': 'Ars'}])
print(num3)

# sample() - функция, которая выбирает k случайных элементов из списка
# возвращает list
num4 = random.sample([1, 2, 3, 4, 5], 2)
print(num4)
