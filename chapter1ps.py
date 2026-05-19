print("""twinkle twinkle little star" \
"how I wonder what you are" \
"up above the world so high"
to print  this statement""")
#tp print a table of 5 using repl
print("5 * 1 = 5*1,"
      )

#prob 2on terminal write python
#to use an external module
#i am installing pyttsx3 module to convert text to speech
#cmd to install pip3 install pyttsx3
# prob 3
#write a python program to print the contects of a directory using os module 
import os

# Specify the directory path
path = "."

# Print contents of the directory
contents = os.listdir(path)

print("Contents of directory:")
for item in contents:
    print(item)

    path = "/Users/yourname/Documents"
    