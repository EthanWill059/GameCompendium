'''
Higher or Lower guessing game
'''

#### Imports #### 
from random import randint # random number generator
import tkinter as tk # tkinter for GUI
from tkinter import * # tkinter for GUI
from sys import platform # need to detect os for something with tk
#################

#### Variables ####
us
###################

#### Mehtods ####
def startup(): # startup method for loading the game

    root = tk.Tk(); print("Higher or Lower window started") # starts a window and confirms this with an output
    root.state("zoomed") ## Makes the window full screen
    root.title("Higher or Lower Game")

    if platform == "darwin": # run if on macos
        pass
    elif platform == "win32": # run if on windows
        root.overrideredirect(1) # windows only code for tkinter

    #### Title at the top #### 
    title = Label(root, text="Higher or Lower")
    title.grid(row=0, column=1, padx=30, pady=50)
    ##########################

    #### Instructions ####
    instructframe = LabelFrame(root, text="Instructions")
    instructframe.grid(row=2, column=0, padx=20, pady=30)

    instructions = Label(instructframe, text="Welcome to Higher or Lower\n Enter a number in the input box to try and guess the mystery number!\n You have a limited amount of guesses so guess well.")
    instructions.grid(row=0, column=0, padx=10, pady=10)
    ######################

    #### Guessing Box and Button ####
    guessinput = Entry(root)
    root.mainloop()
