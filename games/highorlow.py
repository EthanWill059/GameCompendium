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
    guesses = 0
    print("\n!! NEW ROUND !!")

    previous_guesses = [256] # the number 256 is here beacuse the program needs at least one value in the list to run and 256 is an unguessable number so wont effect preformace
    START_GUESSES = 9 
    guesses_left = 9 
    target_num = randint(1,100) # generates random int from 1 - 100
    
    while guesses_left > 0: 
        print("\n")

        flag = False 
        while flag == False: # the loop for asking multipul times after invalid inputs, flag is what I use to exit rather than break
            try:# try to execute this
                user_guess = int(input("Take a guess >> ")) # asks the user to guess # ask for an interger input of how many rounds to be played
                for i in previous_guesses:
                    if user_guess == i:
                        raise ValueError
                if user_guess < -1 or user_guess > 100 or user_guess == 0: # check the number is in range
                    raise ValueError # if it isnt raise an error to be caught by the except block
                else: # only get to here if the input is good
                    previous_guesses.append(user_guess)
                    guesses += 1
                    guesses_left -= 1 
                    flag = True # exit loop with flag

            except ValueError: # catch value errors, raised or unforseen
                print("Enter a valid number and one you haven't guess before!") # error message displayed
        
        if user_guess == -1:
            flag2 = True
            return guesses

        elif user_guess == target_num: # if the user guessed right
            print("Good Job. You got it in {} guesses".format(guesses))
            break # exits loop early

        elif user_guess > target_num: # higher or lower
            print("Go Lower! {} Guesses Left".format(guesses_left))

        else: # higher or lower
            print("Go Higher! {} Guesses Left".format(guesses_left))

    print("The number was {}".format(target_num))
    return guesses

#### Methods ####
def rungame(): # run method for loading the game
    ### Globals ###
    global welcomeplayed
    global flag
    global flag2
    ### Null Varibles ###
    rounds_to_play = 0
    worst_score = 0
    best_score = 0
    avg_score = 0
    roundhistory = []
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
        

    flag = False
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
            guesses = round() # round function, around line 15 - 20
            if guesses > worst_score:
                worst_score = guesses
            if guesses < best_score:
                best_score = guesses
            roundhistory.append(guesses)
    else: # uses the input amount of rounds
        flag = False
        while rounds_to_play > 0 and flag == False: # checks if desired round has been reached yet
            rounds_to_play -= 1 
            guesses = round()
            if guesses > worst_score:
                worst_score = guesses
            elif guesses < best_score:
                best_score = guesses
            roundhistory.append(guesses) 

    print("""
    You just played {} rounds of Higher or Lower!
        Your best amount of guesses was {}
        Your worst amount of guesses was {}
        Your average amount of guesses was {}

        You guessed a total of {} times

        Here are the the amount guesses for each round:
        {}
    """.format(len(roundhistory), best_score, worst_score, sum(roundhistory) / len(roundhistory), sum(roundhistory), roundhistory))

    flag = False # make sure flag is lowered for input loop
    while flag == False: 
        try:
            playagain = int(input("Play Again? [1=yes, 0=no] >> ")) # ask for an interger input of how many rounds to be played
            if playagain < -1: 
                raise ValueError #
            else: 
                flag = True # exit loop with flag
        except ValueError: 
            print("Enter a valid number!") 
    
    if playagain == 1:
        rungame()
    else:
        return

    

    
