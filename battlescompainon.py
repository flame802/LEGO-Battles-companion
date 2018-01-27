#Importing nessisary moduals
from time import sleep
#Defining functions

def startGame(withTimer):
    print("Alright! Get ready to play!")
    sleep(1)
    withTimer = raw_input("Would you like to use a timer if you have set one? y/n")
    if withTimer == "y":
        print("Ok, starting the game with timer")
    else:
        print("Ok, no timer")
    raw_input("Roll a d8 do decide who goes first, when you are done press enter")
    currentPlayer = raw_input("Who going first? " + p1 + " or " + p2 + "? >>>")
    if currentPlayer == p1:
        print(p1 + " is going first!")
    else:
        print(p2 + " is going first!")
    sleep(1)
    if withTimer == "y":
        seconds = 0
        setTimer(seconds)
        startTimer(seconds)
    print(currentPlayer + " is going first")
    while True:
         raw_input("Press enter when " + currentPlayer + "s turn is done")
         sleep(1)
         pointCount(currentPlayer)  #passing currentPlayer to pointCount
         sleep(1)
         if currentPlayer == "p1":
             currentPlayer == "p2"
         else:
            currentPlayer == "p1"
def pointCount(currentPlayer):     #changed to recieve currentPlayer
    points = raw_input("Did " + currentPlayer + " hold any checkpoints this turn?")
    if points == "y":
        numberCheckpoints = raw_input("How many?")
        if currentPlayer == "p1":
            p1bp = p1bp + (numberCheckpoints * 20)
        else:
            p2bp = p2bp + (numberCheckpoints * 20)
        sleep(1)
        if currentPlayer == "p1":
            print(currentPlayer + " has" + p1bp + " battle points")
        else:
            print(currentPlayer + " has" + p2bp + " battle points")
def setTimer(seconds):
    seconds = raw_input("Enter the number of seconds you wish to set a timer for >>>")
    sleep(0.5)
    print("You have set a timer for " + seconds + " seconds")
    sleep(1)
def startTimer(seconds):
    while seconds > 0:
        seconds = seconds - 1
        sleep(1)
        if seconds == 0:
            print("Times up!")
def mainMenu():
    menuSelect = raw_input("||MAIN MENU|| \n" "Name of player 1: " + p1 + "\nName of player 2: " + p2 + "\n" "1:Start Game \n" "2:Set a timer \n" "3:Edit unit stats \n" "4:Quit \n")
    if menuSelect == "1":
        startGame("n")
    elif menuSelect == "2":
        setTimer(0)
        mainMenu()
    elif menuSelect == "3":
        print("Sorry, that function is still being worked on")
        sleep(1)
        mainMenu()
    elif menuSelect == "4":
        exit
#Starting program
print("Welcome to the LEGO Battles Companion")
sleep(1)
print("Programmed by Asa Fasching")
sleep(1)
raw_input("This program will keep track of unit health, armour and battle points. Press enter to continue")
p1 = raw_input("Please enter the name of player 1 >>>")
p2 = raw_input("Please enter the name of player 2 >>>")
p1u = 0
p2u = 0
p1bp = 0
p2bp = 0
sleep(1.5)
print("Now that we have established players let's head to the main menu")
sleep(1)
mainMenu()
 
