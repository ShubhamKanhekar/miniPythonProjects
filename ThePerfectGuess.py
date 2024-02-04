# the computer will generate a random number and the player has to guess it .
import random
import time

from xmlrpc.client import boolean
playagain= True
while playagain:
    quest=random.randint(1,10)
    try:
        guess= int(input("Guess a number from 1 to 10 : "))
    except: 
        guess= int(input("Please input a number : "))

    count=1
    stat= True
    while stat :
        if guess< quest:
            try:
                guess= int(input("A Little Higher Please : "))
            except: 
                guess= int(input("Please input a number : "))
            count+=1

        elif guess > quest:
            try :
                guess= int(input("A Little Lower Please : "))
            except: 
                guess= int(input("Please input a number : "))
            count+=1
        else : 
            print (f"Congratulations, you took {count} attempts to guess the number correctly")
            break


    yORn= input("Do you want to play again? (y/n):")
    if yORn=='y':
        pass
    elif yORn=='n':
        playagain= False
        print("Thank you for playing... see you again sometime..")
        time.sleep(2)
        print("Game ended")
    else : 
        print (" cannot recognise the input... aborting the game...")
        time.sleep(3)
        print("Game ended")
        playagain= False



#METHOD 2 simpler CODE less features (just for practive... method 1 is better and handles all exceptions well)
# randomNum= random.randint(1,10)
# userGuess= None
# guesses= 0
# while userGuess!=randomNum:
#     userGuess= int(input("Enter your guess : "))
#     guesses+=1
#     if userGuess==randomNum:
#         print("Congratulations!!! You found the number.. HipHIpHurray!")
#     else:
#         if (userGuess>randomNum):
#             print("Your guess is wrong... Enter a smaller number ")
#         else:
#             print("Your guess is wrong... Enter a larger number ")
# print(f"You guessed the number in {guesses} guesses.." )

# with open("hiscoreGuessGame.txt", 'r') as hs:
#     hiscore= int(hs.read())
# if (guesses< hiscore):
#     print(f"Woohoo... You have broken the high score. The new hiscore is {guesses} guesses")
#     with open("hiscoreGuessGame.txt", 'w')as hs:
#         hs.write(str(guesses))

