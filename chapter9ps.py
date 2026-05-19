import random
#write a program to check poem exists inthe file3.txt

# with open("file3.txt") as r:
#     texts= r.read()
#     if("poem" in texts):
#         print("we got it")
#     else:
#         print("nahhhh")
# #a game fuction in which give an integer we have to find  high score and current score
# def game():
#     print("you are playing a game")
#     score= random.randint(1,62)
#     print(f"your score{score}")
#     highscorefile = open("highscore", "r+")
#     highscore=highscorefile.read()
    

#     if(highscore==""):
#         highscorefile.write(str(score))
#     elif(int(highscore) < score):
#         highscorefile.write(str(score))
#     highscorefile.close()
# game()

# #write tables now
# for i in range(1,21):
#     def table():
#         text=""
#         for n in range(1,11):
#          text += f"{i}  *  {n} ={i*n}\n"

#         return text

#     files=open(f"files{i}.txt", "w")
#     files.write(table())

#a file contains a word donkey multiple time
file5 = open("file.txt" , "r+")
readfile=file5.read()

if("donkey" in readfile.lower()):
    print("yes thier a a donkey")
    readfile=readfile.replace("donkey" , "#####")
    file5.write(readfile)
    file5.close()
    #do f.write("")
    





        
    

