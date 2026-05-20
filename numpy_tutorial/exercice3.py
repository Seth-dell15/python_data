import numpy as np
#This exercice is about Slicing arrays

#Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:6])


arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr1[:4])#Slicing but from the start to 4
print(arr1[1:])#Slicing but from the 1 to end

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr2[-3:-1])#Negative Slicing

arr3 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr3[1:5:2])#Adding Step
print(arr3[::2])#everything but with step

arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print(arr4[1, 1:4])#Slicing 2D
print(arr4[0:3, 2])# First = Choosen Line and 2nd element = columns
print(arr4[0:3, 1:4]) #ez