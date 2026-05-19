#pip freez give all installed packages
#lamda fuction
square = lambda x: x**2
print(square(5))
#join
a=["a","b","c"]
print("".join(a))
#map
def square(x):
    return x**2
numbers = [1,2,3,4,5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
#format
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
#filter
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
#reduce
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)
