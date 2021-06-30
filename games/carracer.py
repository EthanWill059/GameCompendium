'''
Car Racer
'''

#### Imports #### 
from random import randint # random number generator
from time import sleep
#################

#### Variables ####
flag = False
welcomeplayed = False
###################


#### Functions ####
def race():
    print("racing...") # some fake 5 seconds of loading to slow  it down
    sleep(4)

    global racedistance
    steps = 0 # record the steps
    cars = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0} # record distance the cars have traveled

    for i in range(1,7): # set  the distances for the dictionary
        cars["car{}".format(i)] = racedistance # doing what it saysabove
    
    while True:# check if race is over
        steps += 1
        dice = randint(1,6)# roll the dice

        for i in range(1,7):
            if dice == i:
                cars["car{}".format(i)] -= 1

        for i in range(1,7): # check for winners
            if cars["car{}".format(i)] == 0:
                print("WE HAVE A WINNER!!!")
                sleep(1)
                return i, steps

#### Methods ####
def rungame(): # run method for loading the game
    
    ### Globals ###
    global welcomeplayed
    global racedistance

    ### Varibles ###
    racers = {"car1": "", "car2": "", "car3": "", "car4": "", "car5": "", "car6": ""} # dictionary to remeber who is who

    #####################

    # main #


    if welcomeplayed == False: # stops the welcome message from playing over and over again
        print("""
        Welcome to Car Racer!

        In this game you will choose a car (numbered from 1-6) and a race distance, 
        the computer will then simulate dice rolls and give you the winner.

        At any point you can enter -1 as an input to quit.

        Good Luck!
        """)
        welcomeplayed = True

    for i in range(1,7): # loop to let  people enter their name to a car
        racers["car{}".format(i)] = input("Racer for car #{} <<Leave Blank for no racer >> ".format(i)) # enter the name
    for i in range(1,7): # fill cars that were left blank
        if racers["car{}".format(i)] == "":
            racers["car{}".format(i)] = ("SuperComputer")

    flag = False
    while flag == False:
        try:       
            racedistance = int(input("Please enter a distance for the race (nothing above 15) >> ")) # does what it says on the box
            if racedistance == -1:
                print("Goodbye!")
                return
            elif racedistance <= 15 and racedistance >= 1: # check its a valid distance
                flag = True
            else: # catch errors
                print("Enter a number from range 1-15")
        except ValueError:
            print("Enter a number!")

    winningnumber, steps = race() # gets the winner and the steps from the race

    print("The winner was {} with Car #{}".format(racers["car{}".format(winningnumber)], winningnumber)) # output winnner statements
    print("It took Car #{} {} steps to finish".format(winningnumber, steps)) # output winner statements

    flag = False # make sure flag is lowered for input loop
    while flag == False: # the loop for asking multipul times after invalid inputs, flag is what I use to exit rather than break
        try:# try to execute this
            playagain = int(input("Play Again? [1=yes, 0=no] >> ")) # ask for an interger input of how many rounds to be played
            if playagain < -1: # check the number is in range
                raise ValueError # if it isnt raise an error to be caught by the except block
            else: # only get to here if the input is good
                flag = True # exit loop with flag
        except ValueError: # catch value errors, raised or unforseen
            print("Enter a valid number!") # error message displayed
        
    if playagain == 1:
        rungame()
    else:
        print("Goodbye!")
        return