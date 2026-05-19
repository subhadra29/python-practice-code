#file io
#the things our code give as output to save that as file
file = open("file.txt")
data = file.read
# print(data)
file.close()
#bydefault read
file3= open("file3.txt", "w")
file3.write("hello, bro")
file3.close()

file4=open("file3.txt")
lines= file4.readlines()
print(lines)
file4.close()
#readline reads line according to line
#with staetment

with open("file3.txt") as f:
    print(f.read())
