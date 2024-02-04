
import random
import time
# METHOD 1... USE CLASS 'GAME' TO RETURN BOOLEAN ABOUT THE GAME RESULT OR THE STRING 'TIE' AND THEN PRINT APPROPRIATE RESULT

# def game(a):
#     rand= random.randint(1,3)               #generate random integer using randint function in random module
#     if rand==1: comp= "rock(r)"
#     elif rand==2: comp= 'paper(p)'
#     elif rand==3: comp= 'scissors(s)'
#     print ('computer has chosen : '+ comp)
#     boo= True
#     if (a=='r' and rand==1) or (a=='p' and rand==2) or (a=='s' and rand==3):   #yes we can do this.. just use brackets with care
#         print("it's a tie... both chose "+a)
#         return 'tie'   
#     elif (a=='r' and rand==2) or (a=='p' and rand==3) or (a=='s' and rand==1):
#         #print("loss")
#         boo=False
#     return boo
def game(a):
    rand= random.randint(1,3)               #generate random integer using randint function in random module
    if rand==1: comp= "rock(r)"
    elif rand==2: comp= 'paper(p)'
    elif rand==3: comp= 'scissors(s)'
    print ('computer has chosen : '+ comp)
    boo= True
    if (a=='r' and rand==1) or (a=='p' and rand==2) or (a=='s' and rand==3):   #yes we can do this.. just use brackets with care
        print("it's a tie... both chose "+a)  
    elif (a=='r' and rand==2) or (a=='p' and rand==3) or (a=='s' and rand==1):
        print("You lost the game!!...sorry!")
        boo=False
    else: print("congratulations!!!... You won the game")
    return boo

Playagain= True
while Playagain:
    a= input("Your turn : Choose among rock(r), paper(p) or scissors(s) : ")
    while a!='r'and a!='p' and a!='s':
        print("Invalid Input..... Play Again")
        a = input("Your turn : Choose among rock(r), paper(p) or scissors(s) : ")
        print("you have chosen : " + a)
    GameInitiation= game(a)
    yORn= input("Do you want to play again? (y/n):")
    if yORn=='y':
        pass
    elif yORn=='n':
        Playagain= False
        print("Thank you for playing... see you again sometime..")
        time.sleep(2)
        print("Game ended")
        Playagain= False
    else : 
        print (" cannot recognise the input... aborting the game...")
        time.sleep(3)
        print("Game ended")
        Playagain= False


# stat= game(a)
# if stat=='tie': pass
# elif stat:
#     print("congratulations!!! ....You won")
# else: print("Sorry!... You have lost the game")



#METHOD  2 .. USE PRINT STATEMENTS IN THE CLASS ITSELF

# def game(a):
#     rand= random.randint(1,3)               #generate random integer using randint function in random module
#     if rand==1: comp= "rock(r)"
#     elif rand==2: comp= 'paper(p)'
#     elif rand==3: comp= 'scissors(s)'
#     print ('computer has chosen : '+ comp)
#     boo= True
#     if (a=='r' and rand==1) or (a=='p' and rand==2) or (a=='s' and rand==3):   #yes we can do this.. just use brackets with care
#         print("it's a tie... both chose "+a)  
#     elif (a=='r' and rand==2) or (a=='p' and rand==3) or (a=='s' and rand==1):
#         print("You lost the game!!...sorry!")
#         boo=False
#     else: print("congratulations!!!... You won the game")
#     return boo

# GameInitiation = game(a)
