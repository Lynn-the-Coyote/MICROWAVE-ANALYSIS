import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

#Re_S21_I_1 = np.real(S21_I_1)
#Im_S21_I_1 = np.imag(S21_I_1)

#res_I_1 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 1 res.txt')
S21_I_1 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 1 res.txt', dtype = np.complex_)
res_I_1 = np.arange(5300499968, 5301000192, (5301000192 - 5300499968) / 10001)

S21_I_1_conj = S21_I_1.conjugate()
S21_I_1_dB = []

for i in range(len(S21_I_1)):
    dB = 10 * math.log(float(S21_I_1[i] * S21_I_1_conj[i]), 10)
    S21_I_1_dB.append(dB)

#res_I_2 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 2 res.txt')
S21_I_2 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 2 res.txt', dtype = np.complex_)
res_I_2 = np.arange(5403599872, 5404100096, (5404100096 - 5403599872) / 10001)

S21_I_2_conj = S21_I_2.conjugate()
S21_I_2_dB = []

for i in range(len(S21_I_2)):
    dB = 10 * math.log(float(S21_I_2[i] * S21_I_2_conj[i]), 10)
    S21_I_2_dB.append(dB)

#res_I_3 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 3 res.txt')
S21_I_3 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 3 res.txt', dtype = np.complex_)
res_I_3 = np.arange(5508859904, 5509360128, (5509360128 - 5508859904) / 10001)

S21_I_3_conj = S21_I_3.conjugate()
S21_I_3_dB = []

for i in range(len(S21_I_3)):
    dB = 10 * math.log(float(S21_I_3[i] * S21_I_3_conj[i]), 10)
    S21_I_3_dB.append(dB)

#res_I_4 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 4 res.txt')
S21_I_4 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 4 res.txt', dtype = np.complex_)
res_I_4 = np.arange(5616045056, 5616544768, (5616544768 - 5616045056) / 10001)

S21_I_4_conj = S21_I_4.conjugate()
S21_I_4_dB = []

for i in range(len(S21_I_4)):
    dB = 10 * math.log(float(S21_I_4[i] * S21_I_4_conj[i]), 10)
    S21_I_4_dB.append(dB)

#res_I_5 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 5 res.txt')
S21_I_5 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 5 res.txt', dtype = np.complex_)
res_I_5 = np.arange(5723679232, 5724178944, (5724178944 - 5723679232) / 10001)

S21_I_5_conj = S21_I_5.conjugate()
S21_I_5_dB = []

for i in range(len(S21_I_5)):
    dB = 10 * math.log(float(S21_I_5[i] * S21_I_5_conj[i]), 10)
    S21_I_5_dB.append(dB)

#res_I_6 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II 6 res.txt')
S21_I_6 = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II 6 res.txt', dtype = np.complex_)
res_I_6 = np.arange(5826050048, 5826549760, (5826549760 - 5826050048) / 10001)

S21_I_6_conj = S21_I_6.conjugate()
S21_I_6_dB = []

for i in range(len(S21_I_6)):
    dB = 10 * math.log(float(S21_I_6[i] * S21_I_6_conj[i]), 10)
    S21_I_6_dB.append(dB)

res_I_W = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/freq II wideband.txt')
S21_I_W = np.loadtxt('C:/Users/exton/Desktop/1 MY MASTER PROGRAM LIB/Электродинамика и сверхпроводники/Эксперимент лето 2024/21.08.2024 Nb Res 5 GHz/21.08.2024 Nb Res 5 GHz/II/S21 II wideband.txt', dtype = np.complex_)

S21_I_W_conj = S21_I_W.conjugate()
S21_I_W_dB = []

for i in range(len(S21_I_W)):
    dB = 10 * math.log(float(S21_I_W[i] * S21_I_W_conj[i]), 10)
    S21_I_W_dB.append(dB)

#plt.plot(res_I_1, S21_I_1_dB, 'b', marker = '.', linewidth = 0)
#plt.plot(res_I_2, S21_I_2_dB, 'g', marker = '.', linewidth = 0)
#plt.plot(res_I_3, S21_I_3_dB, 'r', marker = '.', linewidth = 0)
#plt.plot(res_I_4, S21_I_4_dB, 'k', marker = '.', linewidth = 0)
#plt.plot(res_I_5, S21_I_5_dB, 'k', marker = '.', linewidth = 0)
#plt.plot(res_I_6, S21_I_6_dB, 'b', marker = '.', linewidth = 0)
#plt.plot(res_I_W, S21_I_W_dB, 'b', marker = '.', linewidth = 0)

plt.plot((res_I_1 - 5.30077734e9) / 5.30077734e9, S21_I_1_dB, label = 'первый резонанс')
plt.plot((res_I_2 - 5.40385142e9) / 5.40385142e9, S21_I_2_dB, label = 'второй резонанс')
plt.plot((res_I_3 - 5.50910826e9) / 5.50910826e9, S21_I_3_dB, label = 'третий резонанс')
plt.plot((res_I_4 - 5.61629381e9) / 5.61629381e9, S21_I_4_dB, label = 'четвертый резонанс')
plt.plot((res_I_5 - 5.72392884e9) / 5.72392884e9, S21_I_5_dB, label = 'пятый резонанс')
plt.plot((res_I_6 - 5.82629963e9) / 5.82629963e9, S21_I_6_dB, label = 'шестой резонанс')

plt.title('Частотная зависимость S21(f)')
plt.grid(visible = True)
plt.xlabel('Разница частот f и f_res, нормированная на f_res')
plt.ylabel('Коэффицинт прохождения сигнала S21 (dB)')
plt.legend()
plt.show()
