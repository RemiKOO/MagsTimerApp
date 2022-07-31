from tkinter import ttk
import tkinter as tk
from tkinter import *
import random


# Break Page
class break_page:
    def create(self):
        self.exit_break_timer = False
        self.breakcounterVar = tk.StringVar()
        self.breakcounterVar.set("0")
        # Calling Image function with a list of images for this page specifically
        self.imgList = self.make_images(
            ['brk1', 'brk2', 'brk3', 'brk4', 'brk5', 'brk6', 'brk7', 'brk8', 'brk9'])
        breakimage = Label(self, image=random.choice(self.imgList))
        breakimage.place(x=222, y=103)
        # Creating Labels for Break Page
        self.title = ttk.Label(self, text="  Break Time  ",
                               font=('Mangabey', 50, 'underline'))
        self.footer = ttk.Label(
            self, text="© Developed by Luka Jeremic", font=("impact", 8))
        # Placing Labels
        self.footer.place(x=0, y=451)
        self.title.place(x=222, y=0)
        # Creating a Frame with columns for the break timer
        self.breakFrame = ttk.Frame(self)
        self.breakFrame.place(x=105,y=280)
        self.breakFrame.columnconfigure(index=0,weight=1)
        self.breakFrame.columnconfigure(index=1,weight=1)
        self.breakFrame.columnconfigure(index=2,weight=1)

        self.countertext = ttk.Label(
            self.breakFrame, textvariable=self.breakcounterVar, font=('Cambria Bold', 60))
        self.countertext.grid(row=0,column=1)
        self.studytext = ttk.Label(
            self.breakFrame, text="Until Study", font=("Cambria Bold", 22))
        self.studytext.grid(row=1, column=1)

        # Creating Buttons to move from Break Page
        self.buttonStudy = tk.Button(self, text="Start Study", font=(
            "Clip", 25), command=lambda: self.change_page(4))
        self.buttonMenu2 = tk.Button(self, text="Main Menu", font=(
            "Clip", 25), command=lambda: self.change_page(0))
        # Placing Buttons
        self.buttonStudy.place(x=395, y=300, width=230, height=60)
        self.buttonMenu2.place(x=395, y=380, width=230, height=60)
        self.break_timer()
