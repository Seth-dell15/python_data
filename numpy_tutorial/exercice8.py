import numpy as np
#Iterating throught an array

arr = np.array([1, 2, 3])#1D
arr1 = np.array([[1, 2, 3], [4, 5, 6]])#2D
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])#3D

for x in arr2:
  print(x)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

for p in arr3:
  for y in p:
    print(y)

for c in arr2:
  for v in c:
    for z in v:
      print(z)

arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for m in np.nditer(arr4):
  print(m)

  
arr5 = np.array([1, 2, 3])

for w in np.nditer(arr5, flags=['buffered'], op_dtypes=['S']):
  print(w)


arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for o in np.nditer(arr6[:, ::3]):
  print(o)

arr7 = np.array([1, 2, 3])

for idx, az in np.ndenumerate(arr7):
  print(idx, az)

arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx1, ae in np.ndenumerate(arr8):
  print(idx1, ae)
