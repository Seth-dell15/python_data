import numpy as np
#This exercice is about data types

arr = np.array([1, 2, 3, 4])
print(arr.dtype)#int64

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)#<U6 why ? Because < = Endianness(how the data is stored), U = unicode string , 6 =  string longness max

arr2 = np.array([1, 2, 3, 4], dtype='S')

print(arr2) # [b'1' b'2' b'3' b'4']
print(arr2.dtype) #S1

arr3 = np.array([1, 2, 3, 4], dtype='i2') # i2 = size of the int, 1=int8 2=int16 4=int32 8=int64 

print(arr3)
print(arr3.dtype)

# arr = np.array(['a', '2', '3'], dtype='i') #shown because error -> 'a' is not an int

arr4 = np.array([1.1, 2.1, 3.1]) #float

newarr = arr4.astype(int)# float convert to int, we can use int or 'i'

print(newarr)
print(newarr.dtype)

arr5 = np.array([1, 0, 3]) #int

newarr1 = arr5.astype(bool) # convert int to bool

print(newarr1)
print(newarr1.dtype)