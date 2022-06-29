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
        top_left_lbl = Label(self, image=random.choice(self.imgList))
        top_left_lbl.place(x=222, y=103)
        # Creating Labels for Break Page
        self.title = ttk.Label(self, text="  Break Time  ",
                               font=('Mangabey', 50, 'underline'))
        self.studytext = ttk.Label(
            self, text="Until Study", font=("Cambria Bold", 22))
        self.footer = ttk.Label(
            self, text="© Developed by Luka Jeremic", font=("impact", 8))
        self.countertext = ttk.Label(
            self, textvariable=self.breakcounterVar, font=('Cambria Bold', 60))
        # Placing Labels
        self.footer.place(x=0, y=451)
        self.title.place(x=222, y=0)
        self.studytext.place(x=130, y=380)
        if self.breaktimerseconds < 600:
            self.countertext.place(x=125, y=280)
        elif self.breaktimerseconds > 5999:
            self.countertext.place(x=80, y=280)
        else:
            self.countertext.place(x=100, y=280)
        # Creating Buttons to move from Break Page
        self.buttonStudy = tk.Button(self, text="Start Study", font=(
            "Clip", 25), command=lambda: self.change_page(4))
        self.buttonMenu2 = tk.Button(self, text="Main Menu", font=(
            "Clip", 25), command=lambda: self.change_page(0))
        # Placing Buttons
        self.buttonStudy.place(x=380, y=300, width=230, height=60)
        self.buttonMenu2.place(x=380, y=380, width=230, height=60)
        self.break_timer()
