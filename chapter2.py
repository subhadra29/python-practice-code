#variable and datatypes
a=1
b=2
print(a+b)
#variables are like containers that store data values. In Python, you don't need to declare the type of variable, it is determined automatically based on the value assigned to it. For example, if you assign a string value to a variable, it will be treated as a string, and if you assign a number, it will be treated as a number.
#""In Python, is a string; points are floating
#datatypes
a=1 #integer
b=2.5 #float
c="Hello" #string
d=True #boolean
e = None #NoneType

#rules
# 1. Variable names can contain letters, numbers, and underscores
# 2. Variable names cannot start with a number
# 3. Variable names are case-sensitive
# 4. Variable names cannot be reserved keywords
#operators
# 1. Arithmetic operators: +, -, *, /, %, **, //
# 2. Comparison operators: ==, !=, >, <, >=, <=
# 3. Logical operators: and, or, not
# 4. Assignment operators: =, +=, -=, *=, /=, %=,
# 5. Bitwise operators: &, |, ^, ~, <<, >>

b+=5
#here i,m adding 5 to the value of b and assigning the result back to b. So, after this operation, the value of b will be 7.5 (2.5 + 5).
#option for multipl curser
#not changes true to false
#typecasting and type
a=10
pr = type(a)
#typecasting is the process of converting one data type to another
print(pr)

y = "31.4"
e = float(y) # y was a string but now y is a float
#input function
a = input("Enter a number: ")
b = input("Enter another number: ")
c = int(a) + int(b)
print("The sum is: ", c)
#if i don,t do int then it will assume it as a string and won,t give an integer answer


