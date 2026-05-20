import numpy as np
#This exercice will be about summations 

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

arr3 = np.array([1, 2, 3])
arr4 = np.array([1, 2, 3])

newarr1 = np.sum([arr3, arr4])

print(newarr1)

arr5 = np.array([1, 2, 3])
arr6 = np.array([1, 2, 3])

newarr2 = np.sum([arr5, arr6], axis=1)

print(newarr2)

arr7 = np.array([1, 2, 3])

newarr3 = np.cumsum(arr7)#cummulative summation

print(newarr3)