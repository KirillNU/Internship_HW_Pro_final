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

random_matrix = np.random.randint(15, 37, 10)
print(random_matrix)


def sort_ascend(inp_arr):
    def exch_ij(i, j):
        inp_arr[i], inp_arr[j] = inp_arr[j], inp_arr[i]

    n = len(inp_arr)
    replaced = True

    x = -1
    while replaced:
        replaced = False
        x = x + 1
        for i in range(1, n - x):
            if inp_arr[i - 1] > inp_arr[i]:
                exch_ij(i - 1, i)
                replaced = True
    print(f'Переборы: {x}')
    return inp_arr


print(sort_ascend(random_matrix))
