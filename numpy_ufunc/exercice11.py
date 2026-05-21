import numpy as np
#This exercice is about hyperbolic

x = np.sinh(np.pi/2)#we can use sinh() cosh() tanh()

print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x1 = np.cosh(arr)

print(x1)

x2 = np.arcsinh(1.0)# we can also use hyperbolic on arcsin() arccos() and arctan()

print(x2)

arr1 = np.array([0.1, 0.2, 0.5])

x3 = np.arctanh(arr1)

print(x3)