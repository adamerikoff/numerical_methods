#interpolation
#lagrange
import numpy as np
import matplotlib.pyplot as plt

def lagrange_polynomial(x, y, xp):
    n = len(x)
    #n = n - 1
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p = p * ((xp - x[j])/(x[i] - x[j]))
        yp = yp + y[i]* p
    return yp

eps = 1.0

f = lambda x : x * np.cos(np.pi*x/eps)

plt.figure(figsize=(18,6))


plt.subplot(1,3,1)
x_coordinates = [-2, -1.09, -0.5, -0.274, 0, 0.274, 0.5, 1.09, 1.5, 2]
y_coordinates = [-2, 1.047, 0, -0.172, 0, 0.172, 0, -1.047, 0, 2]
plt.scatter(x_coordinates, y_coordinates)
plt.grid(True)
plt.title("Точки рандомные")

plt.subplot(1,3,2)
x = np.arange(-2.0, 2.0, 0.001)
s =  x * np.cos(np.pi*x/eps)
plt.plot(x, s)
plt.title("Оригинальная Функция")
plt.grid(True)

plt.subplot(1,3,3)
x = np.arange(-2.0, 2.0, 0.001)

plt.plot(x, lagrange_polynomial(x_coordinates, y_coordinates, x))
plt.title("Полиномиал Лагранжа")
plt.grid(True)

plt.show()    