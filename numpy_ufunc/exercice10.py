import numpy as np
#This exercice will be about trigonometric functions

x = np.sin(np.pi/2)

print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x1 = np.sin(arr) #we can use sin() tan() and cos()

print(x1)

arr1 = np.array([90, 180, 270, 360])

x2 = np.deg2rad(arr1)# convert degrees to radian

print(x2)

arr2 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x3 = np.rad2deg(arr2)#Convert radian to degrees

print(x3)

x4 = np.arcsin(1.0)# we can also use arcsin() arctan() and arccos()

print(x4)

arr3 = np.array([1, -1, 0.1])

x5 = np.arcsin(arr3)# we can find the angle of all sin values in the array

print(x5)

base = 3
perp = 4

x6 = np.hypot(base, perp)#hypotenues

print(x6)