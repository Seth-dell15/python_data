import numpy as np
#This exercice is about indexing arrays

#1D Dim
arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

#2D Dim
arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr1[0, 1])
print('5th element on 2nd row: ', arr1[1, 4])

#3D Dim
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[1, 0, 2])

#Negative Indexing
arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr3[1, -2])