# Exercise 8 
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of 
# congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

import random
import myFunctions

keepPlaying = True
choiceList = ["Rock", "Paper", "Scissors"]

def playGame(botChoice: str, playerChoice: str):
    if botChoice == playerChoice:
        print("It's a Draw")
    elif botChoice == "Rock" and playerChoice == "Paper" or botChoice == "Scissors" and playerChoice == "Rock" or botChoice == "Paper" and playerChoice == "Scissors":
        print("You Win!")
    elif botChoice == "Rock" and playerChoice == "Scissors" or botChoice == "Scissors" and playerChoice == "Paper" or botChoice == "Paper" and playerChoice == "Rock":
        print("You Lose!")
    else:
        print("Wrong Input")
    print("Bot Chose: " + botChoice)


while keepPlaying == True:
    playerChoice = myFunctions.get_str("Choose between Rock, Paper or Scissors: ")
    botChoice = random.choice(choiceList)
    playGame(botChoice, playerChoice)

    playerInput = myFunctions.get_str("Continue Playing (Y/N)? : ")
    if playerInput.upper() != "Y":
        keepPlaying = False