'''
Задача 5

Даны два списка x и y

x =[-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]

Постройте два графика: plot(x,y) и scatter(x,y) на разных координатных плоскостях.

Постройте еще один график plot(x,y) размером (6, 3) со следущими элементами:

    линиями сетки;
    подписями осей х и y;
    названием графика "Самолет".
'''

import numpy as np
import matplotlib.pyplot as plt

x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]

matrix_x = np.array(x)
matrix_y = np.array(y)

figure, axes = plt.subplots()

axes.scatter(matrix_x, matrix_y, c='red')

plt.xlabel('Переменная X', color='green')
plt.ylabel('Переменная Y', color='blue')

figure.set_figwidth(8)
figure.set_figheight(8)

plt.show()
