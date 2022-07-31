from tkinter import *
import tkinter as tk
from tkinter import ttk


# Homepage Class
class homepage:
    def create(self):
        # Calling Image function with a list of images for this page specifically
        self.imgList = self.make_images(["nac", "dc", 'hsw', 'hg', 'sw', 'ac'])
        # Setting specific images as labels and respective variables.
        self.top_left_img = Label(self, image=self.imgList[0])
        self.mid_left_img = Label(self, image=self.imgList[1])
        self.botm_left_img = Label(self, image=self.imgList[2])
        self.top_right_img = Label(self, image=self.imgList[3])
        self.botm_right_img = Label(self, image=self.imgList[4])
        self.mid_right_img = Label(self, image=self.imgList[5])
        # Placing specific Images in specific their respective positions
        self.top_left_img.place(x=25, y=10)
        self.mid_left_img.place(x=5, y=160)
        self.botm_left_img.place(x=25, y=310)
        self.top_right_img.place(x=560, y=0)
        self.botm_right_img.place(x=600, y=325)
        self.mid_right_img.place(x=565, y=185)
        # All Texts of homepage as labels
        self.Title = ttk.Label(self, text="STimer", font=("LostWages", 60))
        self.SUBTitle = ttk.Label(self, text="    Modernised Study Time Management   ",
                                  font=('Courier New', 13, 'underline'))
        self.Input1req = ttk.Label(self, text="Enter Name", font=("Mangabey", 20))
        self.Input2req = ttk.Label(self, text="Study Duration (Minutes)", font=("Mangabey", 20))
        self.Input3req = ttk.Label(self, text="Break Duration (Minutes)", font=("Mangabey", 20))
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic", font=("impact", 10))
        # Placing Texts/labels
        self.Title.place(x=200, y=0)
        self.SUBTitle.place(x=175, y=95)
        self.Input1req.place(x=225, y=150)
        self.Input2req.place(x=225, y=205)
        self.Input3req.place(x=225, y=260)
        self.footer.place(x=415, y=450)
        # Creating Buttons with called functions
        # Calling ChangePage 1 Function, therefore will open index 1 of the pages in the changePage list

        self.buttonBegin = tk.Button(self, text="Start", font=("Clip", 35), command=lambda: self.submit())
        self.buttonInfo = tk.Button(self, text="Information", font=("Clip", 22), command=lambda: self.change_page(3))
        self.Exit = tk.Button(self, text="Exit App", font=("Clip", 22), command=lambda: self.exitapp())
        # Placing Buttons
        self.buttonBegin.place(x=275, y=310, width=200, height=55)
        self.buttonInfo.place(x=395, y=385, width=170, height=50)
        self.Exit.place(x=180, y=385, width=170, height=50)
        # Inputs
        self.nameinput = ttk.Entry(self, width=20, font=("Cambria bold", 12))
        self.studyminuteinput = ttk.Entry(self, width=8, font=("Cambria bold", 12))
        self.breakminuteinput = ttk.Entry(self, width=8, font=("Cambria bold", 12))
        # Placing Inputs
        self.nameinput.place(x=330, y=154)
        self.studyminuteinput.place(x=440, y=208)
        self.breakminuteinput.place(x=440, y=262)
