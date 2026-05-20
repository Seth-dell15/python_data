import numpy as np
#This exercice is about array reshaping

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)#1D to 2D

print(newarr)

newarr1 = arr.reshape(2, 3, 2)#1D to 3D

print(newarr1)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr1.reshape(2, 4).base)#We want to see if it's a copy or view

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr2 = arr2.reshape(2, 2, -1)# Using unkonwn dimension, if we use 2*2 -1 will calulate the shape

print(newarr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

newarr3 = arr3.reshape(-1)

print(newarr3)