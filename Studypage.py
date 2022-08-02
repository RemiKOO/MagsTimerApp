# Libraries used by this file
from tkinter import ttk
import tkinter as tk


# CLass for Study-Timer Page
class study_page:
    def create(self):
        # Setting up variables
        self.exit_study_timer = False
        self.counterVar = tk.StringVar()
        self.counterVar.set("0")
        # Creating Labels for Texts
        self.title = ttk.Label(self, text="  Study Time  ",
                               font=('Mangabey', 50, 'underline'))
        self.countertext = ttk.Label(
            self, textvariable=self.counterVar, font=('Cambria Bold', 120))
        self.breaktext = ttk.Label(
            self, text="Until Break", font=('Cambria Bold', 22))
        self.footer = ttk.Label(
            self, text="© Developed by Luka Jeremic", font=("impact", 8))
        # Placing the Labels
        self.title.place(x=220, y=0)
        # Grid is used with the timer for symmetry
        self.countertext.grid(row=1, column=1, sticky="s", pady=85)
        self.breaktext.place(x=290, y=280)
        self.footer.place(x=0, y=451)
        # Creating Buttons to move from Study Page
        self.buttonMenu = tk.Button(self, text="Main Menu", font=(
            "Clip", 25), command=lambda: self.change_page(0))
        self.buttonBreak = tk.Button(self, text="Early Break", font=(
            "Clip", 25), command=lambda: self.change_page(2))
        # Placing Buttons
        self.buttonMenu.place(x=120, y=340, width=230, height=60)
        self.buttonBreak.place(x=385, y=340, width=230, height=60)
        self.study_timer()  # Begin the study timer
