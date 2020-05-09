from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def taylor_series(x,fun,x0,n):
	res = S(0)
	for i in range(n+1):
		res += fun.subs(x,x0)*((x-x0)**i)/factorial(i)
		fun = diff(fun,x)
	return res
	


x,y=symbols('x,y')
f = [tan(x),1/(1+x**2),(sin(x)+cos(x))/(1+x**2)]
f_t = [taylor_series(x,f[0],S(0),7),taylor_series(x,f[1],S(0),7),taylor_series(x,f[2],S(0),7)]
xs = [np.linspace(-np.pi/4,np.pi/4,100),np.linspace(-5,5,100),np.linspace(-10,10,1000)]

fig = plt.figure()
a=[]
for j in range(3):
	a.append(fig.add_subplot(1,3,j+1))
	a[j].grid(axis='both')
	a[j].set_title(str(f[j]))
	a[j].plot([i for i in xs[j]],[f[j].subs(x,i) for i in xs[j]])
	a[j].plot([i for i in xs[j]],[f_t[j].subs(x,i) for i in xs[j]])
plt.show()



