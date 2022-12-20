'''
Задача 3

Реализуйте алгоритм сортировки массива пузырьком.

Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного сравнения и обмена соседних
элементов, если предшествующий оказывается больше последующего. В процессе выполнения данного алгоритма элементы
с большими значениями оказываются в конце списка, а элементы с меньшими значениями постепенно перемещаются
по направлению к началу списка. Образно говоря, тяжелые элементы падают на дно, а легкие медленно всплывают
подобно пузырькам воздуха.
'''

import numpy as np
import random

random_matrix = np.random.randint(15, 37, 10)
print(random_matrix)
for i in range(len(random_matrix) - 1):
#    print(random_matrix[i], random_matrix[i + 1])
    if random_matrix[i] < random_matrix[i + 1]:
        pass
    else:
        diff = random_matrix[i] - random_matrix[i + 1]
        random_matrix[i] = random_matrix[i + 1]
        random_matrix[i + 1] = random_matrix[i + 1] + diff
    print(random_matrix[i])
