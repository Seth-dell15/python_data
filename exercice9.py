import numpy as np
#This exercice is about joining arrays in numpy

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))

print(arr3)

arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.concatenate((arr4, arr5), axis=1)

print(arr6)

arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
arr9 = np.stack((arr7, arr8), axis=1)

print(arr9)

arr10 = np.array([1, 2, 3])
arr11 = np.array([4, 5, 6])
arr12 = np.hstack((arr10, arr11))#stack along rows

print(arr12)

arr13 = np.array([1, 2, 3])
arr14 = np.array([4, 5, 6])
arr15 = np.vstack((arr13, arr14))# stack along columns

print(arr15)

arr16 = np.array([1, 2, 3])
arr17 = np.array([4, 5, 6])
arr18 = np.dstack((arr16, arr17)) # stack along height/depth

print(arr18)