import numpy as np
import matplotlib.pyplot as plt

#f = lambda x : 1/(1+x**2)
#actual_sum = np.arctan(5)

f = lambda x : np.sin(x)/x
actual_sum = np.arctan(5)

#f = lambda x: x/(4+x**2)**(1/2)
#actual_sum = np.arctan(5)

a = 0; b = 10; N = 10
n = 10

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,7))

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)


plt.subplot(1,3,1)
plt.plot(X,Y,'b')
x_left = x[:-1] 
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
left_riemann_sum = np.sum(f(x_left) * dx)
plt.title('Left, N = {},\nValue = {},\n ActualValue = {}'.format(N, left_riemann_sum, actual_sum))
plt.grid(True)

plt.subplot(1,3,2)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
plt.title('Midpoint, N = {},\nValue = {},\n ActualValue = {}'.format(N, midpoint_riemann_sum, actual_sum))
plt.grid(True)

plt.subplot(1,3,3)
plt.plot(X,Y,'b')
x_right = x[1:]
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
right_riemann_sum = np.sum(f(x_right) * dx)
plt.title('Right, N = {},\nValue = {},\n ActualValue = {}'.format(N, right_riemann_sum, actual_sum))
plt.grid(True)

plt.show()
