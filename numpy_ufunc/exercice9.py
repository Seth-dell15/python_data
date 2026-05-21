import numpy as np
#This exercice is about GCD (Greatest Common Divisor)

num1 = 6
num2 = 9

x = np.gcd(num1, num2) #Returns: 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3)

print(x)

arr = np.array([20, 8, 32, 36, 16])

x1 = np.gcd.reduce(arr)

print(x1)