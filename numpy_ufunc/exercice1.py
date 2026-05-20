import numpy as np
#This exercice is about creating ufunc function

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add)) # check if ufunc
print(type(np.concatenate)) # check if concatenate
#print(type(np.an_add)) # if we use something that does not exist, it will rise an error.

if type(np.add) == np.ufunc: # we can switch np.add by myadd for exemple
  print('add is ufunc')
else:
  print('add is not ufunc')