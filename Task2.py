'''Задача 2

С помощью встроенных методов библиотеки numpy найдите дату первого понедельника в 2015 году.

Ваш результат может выглядеть так:

image.png

При решении задания вам может пригодиться метод np.busday_offset()

'''

import numpy as np

first_monday_2015 = np.busday_offset('2015-01', 0, roll='forward', weekmask='Mon')
print(f'Первый понедельник в Январе 2015 года:\n{first_monday_2015}')


