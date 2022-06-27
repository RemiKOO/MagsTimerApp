from tkinter import ttk
import tkinter as tk


class pre_study_page:
    def create(self):
        # Creating Labels for Study Page
        self.title = ttk.Label(self, text="  Study Time  ", font=('Mangabey', 50, 'underline'))
        self.breaktext = ttk.Label(self, text="Until Break", font=('Cambria Bold', 22))
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic", font=("impact", 8))
        # Placing Labels
        self.title.place(x=220, y=0)
        self.breaktext.place(x=290, y=280)
        self.footer.place(x=0, y=451)
        # Creating Buttons to move from Study Page
        self.buttonMenu = tk.Button(self, text="Main Menu", font=("Clip", 25), command=lambda: self.change_page(0))
        self.buttonBegin = tk.Button(self, text="Begin Timer", font=("Clip", 25), command=lambda: self.change_page(1))
        # Placing Buttons
        self.buttonMenu.place(x=120, y=340, width=230, height=60)
        self.buttonBegin.place(x=215, y=140, width=300, height=70)

