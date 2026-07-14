import numpy as np

arr= np.arange(1,17)

arr.reshape(4,4)

matrix=arr.flatten()

arr2 = np.random.randint(1,51,10)

arr3 = np.arange(1,21)

print(arr3[arr3 % 3 == 0])
print(arr3[arr3> 12])
print(arr3[(arr3>5) & (arr3 < 15)])
print(arr3[arr3%2 != 0])


marks = np.array([55,90,42,76,81,35,60])

print(marks[marks > 75])
print(marks[marks < 40])
print(np.where(marks==60))