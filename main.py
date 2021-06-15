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

#### MAIN PROGRAM ####

print("""
Welcome to the Game Compendium

Please type a number to choose a game

1) Car Racer Game

2) Higher or Lower Game

""") # prints menu message

while flag == False: # loop until flag is raised
    try: # error catching try block
        user_input = int(input("Make a Selection << -1 to quit >> ")) # input a number, int

        if user_input == 1: # if the input is equal to 1
            pass
        elif user_input == 2: # if the input is equal to 2
            hlgame.run() # runs the higher or lower game
        elif user_input == -1: # if the input is equal to -1
            flag = True # raises flag
        else: # any thing else
            print("Invalid Input, Please enter a Number in range")
    except ValueError: # catching invalid inputs
        print("Invalid Input, Please Enter a Number")

print("Thank You and Goodbye!")