'''
Higher or Lower guessing game
'''

#### Imports #### 
from random import randint # random number generator
#################

#### Variables ####
flag = False
flag2 = False
rounds_to_play = 0
welcomeplayed = False
###################
#### Functions ####
def round():
    global flag2
    print("\n!! NEW ROUND !!")

    START_GUESSES = 9 # varible for working with the starting amount of guesses in the code, makes it more modular
    guesses_left = 9 
    target_num = randint(1,100) # generates random int from 1 - 100
    
    while guesses_left > 0: 
        print("\n")
        guesses_left -= 1 

        flag = False 
        while flag == False: # the loop for asking multipul times after invalid inputs, flag is what I use to exit rather than break
            try:# try to execute this
                user_guess = int(input("Take a guess >> ")) # asks the user to guess # ask for an interger input of how many rounds to be played

                if user_guess < -1 or user_guess > 100: # check the number is in range
                    raise ValueError # if it isnt raise an error to be caught by the except block
                else: # only get to here if the input is good
                    flag = True # exit loop with flag

            except ValueError: # catch value errors, raised or unforseen
                print("Enter a valid number!") # error message displayed
        
        if user_guess == -1:
            flag2 = True
            return

        elif user_guess == target_num: # if the user guessed right
            print("Good Job. You got it in {} guesses".format(START_GUESSES - guesses_left))
            break # exits loop early

        elif user_guess > target_num: # higher or lower
            print("Go Lower! {} Guesses Left".format(guesses_left))

        else: # higher or lower
            print("Go Higher! {} Guesses Left".format(guesses_left))

    print("The number was {}".format(target_num))

#### Methods ####
def run(): # run method for loading the game
    ### Globals ###
    global welcomeplayed
    global flag
    global flag2
    ### Null Varibles ###
    rounds_to_play = 0
    #####################

    # main #

    if welcomeplayed == False: # stops the welcome message from playing over and over again
        print("""
        Welcome to Higher or Lower!

        Higher or lower is a guessing game where you try to guess a secret number
        and I'll tell you if you need to go higher or lower.

        The number will be between 1 - 100 and you'll have 9 guesses
        to try and get it.

        At any point you can enter -1 as an input to quit.

        Good Luck!
        """)
        welcomeplayed = True
        

    
    while flag == False:
        try:# execute below
            rounds_to_play = int(input("How many rounds would you like to play? <<enter 0 for endless>> ")) # ask for an interger input of how many rounds to be played
            if rounds_to_play < -1: # check the number is in range
                raise ValueError # if it isnt raise an error to be caught by the except block
            else: 
                flag = True 
        except ValueError: # catch value errors, raised or unforseen
            print("Enter a valid number!") # error message
    
    
    if rounds_to_play == -1: 
        return 
    elif rounds_to_play == 0: # uses endless rounds
        while flag2 == False: 
            round() # round function, line 15
    else: # uses the input amount of rounds
        flag = False
        while rounds_to_play > 0 and flag == False: # checks if desired round has been reached yet
            rounds_to_play -= 1 # ticking off rounds
            round() # round function, line 15

    print(" SUMMMARY WILL GO HERE ## DEV MESSAGE ## ")

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
        run()
    else:
        return

    

    
