# Libraries used by this file
from tkinter import ttk
import tkinter as tk


# Class for Pre-Information Page
class Pre_information_page:
    def create(self):
        # Creating Labels
        self.infotitle = ttk.Label(self, text="  Information  ",
                                   font=('Mangabey', 50, 'underline'))
        self.nametext = ttk.Label(self, text="Enter Name",
                                  font=('Mangabey', 25))
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic",
                                font=("impact", 8))
        # Placing Labels
        self.infotitle.place(x=225, y=0)
        self.nametext.place(x=310, y=130)
        self.footer.place(x=0, y=451)
        # Make an Entry for NameInput
        self.nameinput = ttk.Entry(self, width=13, font=("Cambria bold", 13))
        # Place the Entry
        self.nameinput.place(x=227, y=185)
        # Create buttons to move from Pre-Information page
        self.buttonMain = tk.Button(self, text="Main Menu", font=('Clip', 22),
                                    command=lambda: self.change_page(0))
        self.finduser = tk.Button(self, text="Find User", font=('Clip', 16),
                                  command=lambda:
                                      self.getdata(self.nameinput.get()))
        # Place the buttons
        self.buttonMain.place(x=240, y=360, width=260, height=60)
        self.finduser.place(x=377, y=185, width=130, height=36)
