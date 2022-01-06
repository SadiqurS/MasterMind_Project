'''
Sadiqur. Sakib
period #8
Mastermind project
'''


import random


print ("Guess the correct numbers in 10 tries good luck.")


numlist = ["1","2","3","4","5","6","7","8","9","0"]
attempts = 0
game = True

# this generates the random numbers
numbers = random.sample(numlist,4)


#this is what allows player to guess the numbers
while game:
  correct_number = ""
  guessed_number= ""
  player_guess = input().upper()
  attempts += 1

  #this determines whether or not the players answer is correct with the random numbers generated
  if len(player_guess) != len(numbers):
     print ("The answer has to be in 4 digits follow them diretions!!!")
     while(True):
      for i in range(4):
         if player_guess[i] not in numlist:
            print ("Look up what colors you can use in this game. You are not a daltonist, are you?")
            continue

  # this compares the players code the the numbers and checks to see if any of the numbers the player gave is matched with the ramdon set of numbers
  if correct_number != ("XXXX"):
     for i in range(4):
        if player_guess[i] == numbers[i]:
           correct_number += ("X")
        if  player_guess[i] != numbers[i] and player_guess[i] in numbers:
           guessed_number += ("O")
     print (correct_number +  guessed_number )
#If the player gets the correct answer on first attempt this process will be carried out
  if correct_number == ("XXXX"):
     if attempts == (1):
        print ("Pure luck boi!")
     #If the player guesses the correct digits within the given range of guesses this process will be carried out
     else:
        print ("Congrats dude you rock!!!")
     game = (False)
#this tells player that they are wrong and shows the correct digits generated in the game
  if (attempts >= 1 and attempts <10 and correct_number != "XXXX"):
     print ("go again: ")
  elif attempts >= (10):
     print ("You are a failure, but The correct numbers are: " + str(numbers))
