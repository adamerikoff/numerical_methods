import numpy as np
import matplotlib.pyplot as plt

def get_y_matrix(ys):
    n_xs = len(xs)
    n_splines = n_xs - 1
    n_derivatives = n_splines - 1
    n_equations = n_splines*2
    matrix_size = n_derivatives + n_equations + 1

    y_matrix = []
    y_matrix.append([ys[0]])
    for i in range(len(ys)-1):
        index = i + 1
        y_matrix.append([ys[index]])
        y_matrix.append([ys[index]])
    y_matrix.pop()
    for i in range(matrix_size - n_equations):
        y_matrix.append([0])

    return y_matrix

def get_matrix(xs):
    n_xs = len(xs)
    n_splines = n_xs - 1
    n_derivatives = n_splines - 1
    n_equations = n_splines*2
    matrix_size = n_derivatives + n_equations + 1

    matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]

    for i in range(n_splines):
        index = i*2

        head = [0 for col in range(i*3)]
        body1 = [xs[i]*xs[i], xs[i], 1]
        body2 = [xs[i+1]*xs[i+1], xs[i+1], 1]
        tail = [0 for col in range(matrix_size-3-i*3)]
        matrix[index] = head + body1 + tail
        matrix[index+1] = head + body2 + tail
    for i in range(n_derivatives):
        x = xs[i+1]

        head = [0 for col in range(i*3)]
        tail = [0 for col in range(matrix_size-6-i*3)]

        body = [2*x, 1, 0, -2*x, -1,0]

        matrix[10+i] = head + body + tail
    matrix[-1][0] = 1 
    return matrix

def get_value(xs, x, splines):
    index = 0
    for i in range(len(xs)):
        if x > xs[i]:
            index = i
    i = index*3
    a = splines[index*3]
    b = splines[i+1]
    c = splines[i+2]
    value = a*x*x + b*x + c
    return value 

float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

xs = [0, 3.4, 12.18, 17.6, 23.55, 30]
ys = [0, 5.03, 5.188, -2.956, -8, -2.235] 


xm = np.array(get_matrix(xs))
ym = np.array(get_y_matrix(ys))

x_i = np.linalg.inv(xm)

result = np.dot(x_i, ym)

eps = 1.0

plt.figure(figsize=(18,6))

plt.subplot(1,3,1)
plt.scatter(xs, ys)
plt.grid(True)
plt.title("Точки рандомные")

plt.subplot(1, 3, 2)
x = np.arange(0, 30, 0.1)
s =  1/8 * np.sin(1/5*x)
plt.plot(x, s)
plt.title("Оригинальная Функция")
plt.grid(True)


plt.subplot(1,3,3)
x = np.arange(0, 30, 0.01)

y = []
for i in range(len(x)):
   y.append(get_value(xs, x[i], result))

plt.scatter(xs, ys)
plt.plot(x, y)
plt.title("Квадратичный Сплайн")
plt.grid(True)

plt.show()  

