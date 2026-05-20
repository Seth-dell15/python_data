import numpy as np
#This exercice will be about rounding decimals

arr = np.trunc([-3.1666, 3.6667])# we can also use .fix for truncation / return the float number closest to zero

print(arr)

arr1 = np.around(3.1666, 2)# Rounding function increments preceding digit or decimal by 1

print(arr1)

arr2 = np.floor([-3.1666, 3.6667])# Floor function rounds off decimal to nearest lower integer

print(arr2)

arr = np.ceil([-3.1666, 3.6667])# Ceil function rounds off decimal to nearest upper integer

print(arr)