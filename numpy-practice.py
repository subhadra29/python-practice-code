import numpy as np

arr = np.array([5,10,15,20,25])

newarr= arr*3
print(newarr)


print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.sum())

new1arr= np.array([[1, 2],
                  [3 ,4],
                  [5,6]])


newarr2=np.arange(1,100)

print(newarr2.sum())
print(newarr2.min())
print(newarr2.max())
print(newarr2[::2])