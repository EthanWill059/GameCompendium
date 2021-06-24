'''
The menu file for the Game compendium project
'''
#### Functions ####
def highorlow():
    print("game ran")
    
def carracer():
    print("game ran")
    
#### MAIN PROGRAM ####

while True: # loop until flag is raised
    print("""
    Welcome to the Game Compendium

    Please type a number to choose a game

    1) Car Racer Game

    2) Higher or Lower Game

    """)
        

    user_input = int(input("Make a Selection << -1 to quit >> ")) # input a number, int

    if user_input == 1: # if the input is equal to 1
        carracer()
            
    elif user_input == 2: # if the input is equal to 2
        highorlow()

    elif user_input == -1: # if the input is equal to -1
        break

print("Thank You and Goodbye!")
