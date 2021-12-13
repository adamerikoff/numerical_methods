#interpolation
#lagrange
import numpy as np
import matplotlib.pyplot as plt

class Equation:
    def __init__(self, x):
        self.x = x
        
 
    def get_array(self):
        array = []

        array.append(self.x**3)
        array.append(self.x**2)
        array.append(self.x)
        array.append(1)

        return array

class Derivative():
    def __init__(self, x1):
        self.x1 = x1
        
 
    def get_der1(self):
        array = []

        array.append(3 * self.x1**2)
        array.append(2 * self.x1)
        array.append(1)
        array.append(0)

        array.append(-3 * self.x1**2)
        array.append(-2 * self.x1)
        array.append(-1)
        array.append(0)

        return array

    def get_der2(self):
        array = []

        array.append(6 * self.x1)
        array.append(2)
        array.append(0)
        array.append(0)

        array.append(-6 * self.x1)
        array.append(-2)
        array.append(0)
        array.append(0)

        return array
    

class SplineMatrix:
    def __init__(self, xs, ys):
        m_size = (len(xs)-1)*4

        self.xs = xs
        self.ys = ys
        self.matrix_size = m_size
        self.x_matrix = []
        self.y_matrix = []
        self.result = []

        self.create_matrix()
        self.create_y_matrix()
        self.calculate_coef()

    def guess_the_value(self, x):
        index = 0
        for i in range(len(self.xs) - 1):
            if x > xs[i]:
                index = i
        i = index*4

        a = self.result[i][0]
        b = self.result[i+1][0]
        c = self.result[i+2][0]
        d = self.result[i+3][0]

        value = a * x**3 + b * x**2 + c * x + d
        return value 

    def calculate_coef(self):

        x_i = np.linalg.inv(np.array(self.x_matrix))
        result = np.dot(x_i, np.array(self.y_matrix))
        self.result = result

    def get_eqs(self):
        eqs = []
        for i in range(len(self.xs)):
            if i > 0 and i < len(self.xs)-1:
                eqs.append(Equation(xs[i]).get_array())
                eqs.append(Equation(xs[i]).get_array())
            else:
                eqs.append(Equation(xs[i]).get_array())
        matrix_eqs = []
        for i in range(0, len(eqs), 2):
            head_size = i*2
            head = [0 for col in range(head_size)]
            body1 = eqs[i]
            body2 = eqs[i+1]
            tail = [0 for col in range(self.matrix_size-4-head_size)]
            m1 = head + body1 + tail 
            m2 = head + body2 + tail
            matrix_eqs.append(m1)
            matrix_eqs.append(m2)
            
        return matrix_eqs

    def get_ders(self):
        x_values = self.xs.copy()
        del x_values[0]
        del x_values[-1]

        ders1 = []
        ders2 = []

        m_ders = []

        for i in range(len(x_values)):
            ders1.append(Derivative(x_values[i]).get_der1())

        for i in range(len(ders1)):
            head_size = 4*i
            head = [0 for col in range(head_size)]
            body = ders1[i]
            tail = [0 for col in range(self.matrix_size-8-head_size)]
            m = head + body + tail 
            m_ders.append(m)

        for i in range(len(x_values)):
            ders2.append(Derivative(x_values[i]).get_der2())
        
        for i in range(len(ders2)):
            head_size = 4*i
            head = [0 for col in range(head_size)]
            body = ders2[i]
            tail = [0 for col in range(self.matrix_size-8-head_size)]
            m = head + body + tail 
            m_ders.append(m)

        return m_ders

    def get_matrix(self):
        matrix = []
        eqs = self.get_eqs()
        ders = self.get_ders()
        for i in eqs:
            matrix.append(i)
        for i in ders:
            matrix.append(i)
        #boundary conditions matrice rows
        b1 = [0 for col in range(self.matrix_size)]
        b2 = [0 for col in range(self.matrix_size)]
        
        b1[1] = 2
        b2[-4] = 3*2*self.xs[-1]
        b2[-3] = 2
        matrix.append(b1)
        matrix.append(b2)

        return matrix

    def create_matrix(self):     
        self.x_matrix = self.get_matrix()

    def create_y_matrix(self):
        m = []
        y_values = self.ys.copy()
        del y_values[0]
        del y_values[-1]
        m.append([ys[0]])
        for y in y_values:
            m.append([y])
            m.append([y])
        m.append([ys[-1]])

        for i in range(self.matrix_size - len(m)):
            m.append([0])
        self.y_matrix = m


float_formatter = "{:.2f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

#Указываются точки в этих arrays
#И программа сама сделает все!
xs = [0, 1, 2, 3, 4, 5, 7, 9]
ys = [21, 24, 24, 18, 16, 12, 8, 2]

spline_main = SplineMatrix(xs, ys)

plt.figure(figsize=(15,6))

plt.subplot(1,2,1)
plt.scatter(xs, ys)
plt.grid(True)
plt.title("Точки рандомные")


plt.subplot(1,2,2)
x = np.arange(xs[0], xs[-1], 0.01)
y = []
for i in range(len(x)):
    y.append(spline_main.guess_the_value(x[i]))
plt.scatter(xs, ys)
plt.plot(x, y)
plt.title("Кубический Сплайн")
plt.grid(True)

plt.show()  

