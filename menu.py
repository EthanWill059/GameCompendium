'''
The menu file for the Game compendium project
'''

#### IMPORTS ####
import tkinter as tk
from tkinter import *
from tkinter import ttk
#################

#### Functions ####
def rungame():
    print("GAME BEING RUN")

#### MAIN PROGRAM ####

root = tk.Tk(); print("Window Started") # defines the window itself, root is the parent window and prints a notification to notate this event
root.title("Game Compendium") # sets the title shown in the top bar

title = Label(root, text="Game Compendium") # Creates the actual title in the menu
title.grid(row=0, column=0, padx=20, pady=30, sticky=NSEW) # places the title in the grid location (0,0)

games_frame = LabelFrame(root, text="Games") # creates an onscreen box to clean up the GUI contains the run buttons for games
games_frame.grid(row=1, column=0, padx=50, pady=30) # places this on screen at grid location (1,0)

cargame_button = Button(games_frame, text="Car Racer Game", command=rungame) # first game button, starts car racer
cargame_button.grid(row=0, column=0, padx=10, pady=20, sticky=NSEW)

highlow_button = Button(games_frame, text="Higher or Lower Game", command=rungame) # first game button, starts car racer
highlow_button.grid(row=1, column=0, padx=10, pady=20, sticky=NSEW)

quit_button = Button(root, text="QUIT", command=quit)
quit_button.grid(row=3, column=0, padx=10, pady=20, sticky=EW)

root.mainloop()## Runs a loop for the window 