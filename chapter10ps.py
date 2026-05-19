class programmer:
    workingat= "microsoft"
    language="python"
    dateofjoining="29/09/2007"
    def __init__(self , name , dob, pin):
        self.name=name
        self.dob=dob
        self.pin=pin

        

rohan=programmer("harry",29,00)
print(rohan.name)
#write a class calculator capeble
class calculator:
    
        
    def __init__(self,number):
        
        self.number=number
    def square(self):
       print("the square of the number is: ", self.number*self.number)
    def root(self):
        print("the root is",self.number**1/2 )
    @staticmethod
    def hellO():
        print("hello there")
class train:
    def __init__(self,name,seat,price):
        self.name=name
        self.seat=seat
        self.price=price

        
    def book(self):
        print("it is used to book", self.name)

    def status(self):
        print("this seat number is,", self.seat)



    
