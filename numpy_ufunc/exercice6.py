import numpy as np
#This exercice will be about Products

arr = np.array([1, 2, 3, 4]) # 1*2*3*4 = 24 

x = np.prod(arr)

print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x1 = np.prod([arr1, arr2]) 

print(x1)#Product of 2 array

arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([5, 6, 7, 8])

newarr = np.prod([arr3, arr4], axis=1)

print(newarr)

arr5 = np.array([5, 6, 7, 8])

newarr1 = np.cumprod(arr5) #Cummulative Product

print(newarr1)