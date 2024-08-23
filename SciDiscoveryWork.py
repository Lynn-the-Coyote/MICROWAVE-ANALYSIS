import matplotlib.pyplot as plt
import numpy as np
import math
import cmath


def f(x, z):
    C = z * 10 ** -15
    C2 = z * 10 ** -15
    Zc = 1/(1j * 2 * math.pi * x * C)
    vp = 1.066 * 10 ** 8
    Zc2 = 1/(1j * 2 * math.pi * x * C2)

    teta = (2 * math.pi * x * (2 * 10 ** -2)) / vp

    a = np.array([[1, Zc],
                  [0, 1]])

    b = np.array([[math.cos(teta), 1j * 75 * math.sin(teta)],
                  [1j * math.sin(teta) / 75, math.cos(teta)]])

    e = np.array([[1, Zc2],
                  [0, 1]])

    c = (a.dot(b)).dot(e)

    S21 = 2/(c[0, 0] + c[0, 1]/75 + 75 * c[1, 0] + c[1, 1])

    #for  calculating the line without the capacities on the in and out of the testing line change the 'c' array to 'b'
    # else you have to change the scale (line 49) to see the whole graph

    S21c = S21.conjugate()
    return 10 * math.log(float(S21 * S21c), 10)


y1 = []
y2 = []
y3 = []
y4 = []

t = np.arange(0.0000001, 3., 0.000005)
for i in t:
    y1.append(f(i * 10 ** 9, 5))
    y2.append(f(i * 10 ** 9, 25))
    y3.append(f(i * 10 ** 9, 50))
    y4.append(f(i * 10 ** 9, 1))

print(y1)

plt.plot(t, y4, 'c', label='Ck = 1 фФ, Q = 5,97 * 10^6')
plt.plot(t, y1, 'b', label='Ck = 5 фФ, Q = 2,01 * 10^5')
# plt.plot(t, 0, 'r--')
plt.plot(t, y2, 'g', label='Ck = 25 фФ, Q = 832')
plt.plot(t, y3, 'r', label='Ck = 50 фФ, Q = 217')

plt.ylabel('10lg|S21|^2 (dB)')
plt.xlabel('Частота (ГГц)')

plt.title('Зависимость S21(f)')
plt.ylim(-150, 1)
plt.grid(visible=True)
plt.legend()
plt.show()