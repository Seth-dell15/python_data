import numpy as np
#This exercice will be about simple arithmetic

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2) #Addition

print(newarr)

arr3 = np.array([10, 20, 30, 40, 50, 60])
arr4 = np.array([20, 21, 22, 23, 24, 25])

newarr1 = np.subtract(arr3, arr4)#Substraction

print(newarr1)

arr5 = np.array([10, 20, 30, 40, 50, 60])
arr6 = np.array([20, 21, 22, 23, 24, 25])

newarr2 = np.multiply(arr5, arr6)#Multiplication

print(newarr2)

arr7 = np.array([10, 20, 30, 40, 50, 60])
arr8 = np.array([3, 5, 10, 8, 2, 33])

newarr3 = np.divide(arr7, arr8)#Division

print(newarr3)

arr9 = np.array([10, 20, 30, 40, 50, 60])
arr10 = np.array([3, 5, 6, 8, 2, 33])

newarr4 = np.power(arr9, arr10)#Power

print(newarr4)

arr11 = np.array([10, 20, 30, 40, 50, 60])
arr12 = np.array([3, 7, 9, 8, 2, 33])

newarr5 = np.mod(arr11, arr12)# Remainder, can be .mod or .remainder

print(newarr5)

arr13 = np.array([10, 20, 30, 40, 50, 60])
arr14 = np.array([3, 7, 9, 8, 2, 33])

newarr6 = np.divmod(arr13, arr14)

print(newarr6)

arr15 = np.array([-1, -2, 1, 2, 3, -4])

newarr7 = np.absolute(arr15)#Absolute value

print(newarr7)