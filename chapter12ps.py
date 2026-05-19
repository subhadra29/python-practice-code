try:
    with open('chapter12ps.py', 'r') as file:
        print(file.read())
except Exception as e:
    print(e)

try:
    with open("chapter12ps.py","r") as file:
        print(file.read())
except Exception as e:
    print(e)

#2nd
l =[1,2,3,4,5,6,7,8]

for i, item in enumerate(l):
    if i==2 or i==4 or i==6:
        print(item)
#list comparision
n=3
table=[n*i for i in range(1,11)]
print(table)
#4th
try:
    a=int(input("write a number"))
    b=int(input("write another number"))
    print("the division is", a/b)
except ZeroDivisionError as e:
    print("infinty")
#5th
table=[n*i for i in range(1,11)]