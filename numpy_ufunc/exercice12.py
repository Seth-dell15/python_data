import numpy as np
#This exercice is about set used for operation using intersections, union and difference operations 

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)#we create a set

print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)# union

print(newarr)

arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([3, 4, 5, 6])

newarr1 = np.intersect1d(arr3, arr4, assume_unique=True)#intersection

print(newarr1)

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr2 = np.setdiff1d(set1, set2, assume_unique=True)#found the difference in the first set

print(newarr2)

set3 = np.array([1, 2, 3, 4])
set4 = np.array([3, 4, 5, 6])

newarr3 = np.setxor1d(set3, set4, assume_unique=True)#found the difference between the two set

print(newarr3)