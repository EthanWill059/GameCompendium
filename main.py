'''
The menu file for the Game compendium project
'''

#### IMPORTS ####
##
import games.carracer as cargame# imports the car racer game
import games.highorlow as hlgame# imports the higher or lower game
#################

#### Functions ####


#### Varibles ####
flag = False # used for exiting a while loop without break
welcomeplayed = False

#### MAIN PROGRAM ####

while flag == False: # loop until flag is raised
    try: # error catching try block
        if welcomeplayed == False: # stops the welcome message from playing over and over again
            print("""
    Welcome to the Game Compendium

    Please type a number to choose a game

    1) Car Racer Game

    2) Higher or Lower Game

        """)
        welcomeplayed = True

        user_input = int(input("Make a Selection << -1 to quit >> ")) # input a number, int

        if user_input == 1: 
            welcomeplayed = False # play the welcome message when user returns
            cargame.rungame()
        elif user_input == 2:
            welcomeplayed = False # plays welcome message on user return
            hlgame.rungame() # runs the higher or lower game
        elif user_input == -1: 
            flag = True # raises flag
        else: 
            print("Invalid Input, Please enter a Number in range")
    except ValueError: # catching invalid inputs
        print("Invalid Input, Please Enter a Number")

print("Thank You and Goodbye!")