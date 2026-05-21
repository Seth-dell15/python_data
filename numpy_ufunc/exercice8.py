import numpy as np
#This exercice is about LCM (Lowest Common Multiple)

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)# Returns: 12 because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12)

arr = np.array([3, 6, 9])

x1 = np.lcm.reduce(arr)

print(x1) #Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18)

arr1 = np.arange(1, 11)

x2 = np.lcm.reduce(arr1)

print(x2)