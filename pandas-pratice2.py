import pandas as pd

studentcv= pd.read_csv("students.csv")

print(studentcv.shape)
print(studentcv.columns)
print(studentcv.info())
print(studentcv.describe())
print(studentcv["Marks"].max())

print(studentcv["Marks"].min())

print(studentcv["Marks"].mean())

print(studentcv[(studentcv["Marks"]) > 75 & (studentcv["Attendance"]) > 90])

Grade=[]

for mark in studentcv["Marks"]:
    if(mark> 90):
        Grade.append("A")
    elif(mark>75 and mark<90):
        Grade.append("B")
    else:
        Grade.append("C")