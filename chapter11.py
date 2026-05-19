#inheritance
class parent:
    def rohan():
        print("thei maa ki cht")
class raju(parent):
    def gandu():
        print("tum ek gandu ho")
#to access any property of parent class in child class we use 
#super() function

#class methodes
#to show direct classmethodes we use @classmethod
class student:
    school="sps"
    @classmethod
    def change_school(cls,new_school):
        cls.school=new_school
s1=student()
print(s1.school)
s1.change_school("sps")
print(s1.school)

#property decorator
