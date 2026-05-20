import numpy as np
# This exercice is about copy and view

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
y = arr.copy()

print(arr)
print(x)
print(y)

arr1 = np.array([1, 2, 3, 4, 5])
c = arr1.view()
arr1[0] = 42

print(arr1)
print(c)

arr2 = np.array([1, 2, 3, 4, 5])
z = arr2.view()
z[0] = 31

print(arr2)
print(z)

arr3 = np.array([1, 2, 3, 4, 5])

g = arr3.copy()
h = arr3.view()

print(g.base) #Return None because does not own
print(h.base) #Return original array