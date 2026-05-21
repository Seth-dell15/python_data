import numpy as np
#This exercice is about differences

arr = np.array([10, 15, 25, 5]) 

newarr = np.diff(arr)#-> 15-10 25-15 5-25

print(newarr)

arr1 = np.array([10, 15, 25, 5])

newarr1 = np.diff(arr1, n=2)# n=2 means we do the diff 2 times

print(newarr1)