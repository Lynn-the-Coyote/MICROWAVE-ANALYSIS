import matplotlib.pyplot as plt
import numpy as np
import math
import cmath


def f(x, z):
    C = 50 * 10 ** -15
    C2 = 50 * 10 ** -15
    Zc = 1/(1j * 2 * math.pi * x * C)
    cv = 3 * 10 ** 8
    Zc2 = 1/(1j * 2 * math.pi * x * C2)

    teta = (2 * math.pi * x * (5 * 10 ** -2) * math.sqrt(4)) / cv

    a = np.array([[1, Zc],
                  [0, 1]])
    b = np.array([[math.cos(teta), -1j * z * math.sin(teta)],
                 [-1j * math.sin(teta) / z, math.cos(teta)]])
    e = np.array([[1, Zc2],
                  [0, 1]])
    c = (a.dot(b)).dot(e)

    S21 = 2/(c[0, 0] + c[0, 1]/50 + 50 * c[1, 0] + c[1, 1])
    #for  calculating the line without the capacities on the in and out of the testing line change the 'c' array to 'b'

    S21c = S21.conjugate()
    return 10 * math.log(float(S21 * S21c), 10)


y1 = []
y2 = []
y3 = []
t = np.arange(0.000000001, 20., 0.001)
for i in t:
    y1.append(f(i * 10 ** 9, 50))
    y2.append(f(i * 10 ** 9, 100))
    y3.append(f(i * 10 ** 9, 200))
print(y1)
plt.plot(t, y1, 'g', label='50')
# plt.plot(t, 0, 'r--')
plt.plot(t, y2, 'b', label='100')
plt.plot(t, y3, 'r', label='200')
plt.ylabel('S21 (dB)')
plt.xlabel('Частота (ГГц)')
plt.title('Зависимость S21(f)')
plt.ylim(-8, 1)
plt.grid(visible=True)
plt.legend()
plt.show()



#
#
# epochs = 100
# t = np.arange(0., 5., 0.2)
# print(t)
# y = [12, 2, 5, 10, 2, 5]
# h = [32, 2, 55, 2, 10, 5]
# plt.plot(t, t ** 2,'b' ,label='Smoothed training acc')
#
# plt.title('Training and validation accuracy')
# plt.legend()
#
# plt.title('Training and validation loss')
# plt.legend()
#
# plt.figure()
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 50
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
#
#
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
#
# plt.figure(figsize=(9, 3))
#
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
#
# plt.show()