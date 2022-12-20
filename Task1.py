'''

Задача 1

Создайте двумерный массив размерностью 3 на 4, состоящий из случайных целых чисел от 15 до 37.

Требуется создать новый массив той же размерности (3,4), значения которого будут зависеть от значений исходного массива
и могут принимать одно из трех возможных значений:

    "small", для значений исходного массива меньше 20;
    "medium", для значений исходного массива в промежутке [20, 30];
    "large", для значений исходного массива больше 30.

Пример:

Исходный массив:

[[35 36 25 34]
 [26 27 23 29]
 [28 34 33 17]]

[['large' 'large' 'medium' 'large']
 ['medium' 'medium' 'medium' 'medium']
 ['medium' 'large' 'large' 'small']]
'''

import numpy as np
import random

random_matrix = np.random.randint(15, 37, (3, 4))
final_matrix = np.empty((3, 4), 'U8')
print(random_matrix, '\n')

for i in range(3):
    for j in range(4):
        if random_matrix[i][j] < 20:
           final_matrix[i][j] = 'small'
        elif 20 <= random_matrix[i][j] <=30:
            final_matrix[i][j] = 'medium'
        else:
            final_matrix[i][j] = 'large'
print(final_matrix)

