#write a python program to display a user entered name followed by Good Afternoon 
a = input("plese enter your name")

print("good afternoon" , a)
#or
print(f"good afternoon {a}")

#use + 
b = input("plese enter your name")
c = input("plese enter the date of selection")
print(f"Dear {b} \n you are selected! \n {c}")
#or
# print(c.replace(f"{b}", "harry").replace(f"{c}", "24th sept"))
#write a program to detect double space in a string
d = "subhadra. 1  224"
print(d.find("  "))
#if -1 comes then no double space
#to replace the double space to triple space
print(d.replace("  " , " "))
#write a program using escape sequance character


