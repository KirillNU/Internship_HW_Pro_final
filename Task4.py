'''
Задача 4

Нарисуйте график рассеяния со случайным распределением по осям X и Y.
'''

import numpy as np
import matplotlib.pyplot as plt

''' случайные координаты точек '''
x = np.random.rand(1000) * 100  # x - координаты
y = np.random.rand(1000) ** 0.5  # y - координаты

''' область и подобласть рисования '''
figure, axes = plt.subplots()

''' цвета точек '''
axes.scatter(x, y, c='green')

''' цвет фона в областей Figure и Axes '''
figure.set_facecolor('grey')
axes.set_facecolor('lightblue')

''' заголовок для Axes '''
# axes.set_title('График рассеяния')
plt.title('График рассеяния', color='red', fontsize= 16)  # Команда .title() - и график подписан указанным в скобках именем
plt.xlabel('Переменная X', color='blue')  # Команда .xlabel() добавит надпись только для оси x
plt.ylabel('Переменная Y', color='magenta')

''' ширина и высота "Figure" '''
figure.set_figwidth(7)
figure.set_figheight(7)

plt.show()