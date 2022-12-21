import numpy as np
import matplotlib.pyplot as plt

x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]

matrix_x = np.array(x)
matrix_y = np.array(y)

figure, axes = plt.subplots(1, 2)
figure.set_facecolor('grey')

axes[0].scatter(matrix_x, matrix_y, c='green', marker='v')
axes[1].plot(matrix_x, matrix_y, ':r', lw=4)
plt.title('Это самолёт', color='blue')
axes[1].grid()

# figure.set_figwidth(12)
# figure.set_figheight(10)

plt.show()
