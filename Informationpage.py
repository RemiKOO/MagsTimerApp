# Libraries used by this file
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


# Class of THE Information Page
class information_page:
    def create(self):  # Create the page
        # Opening Image so that when page is refreshed,
        # the image will refresh as well (For Light/Dark Theme)
        self.studygraph(self.datalist)
        self.image = Image.open('./img/graph.png')
        # Resizing the image to fit into the window aesthetically
        self.graphimage = self.image.resize((380, 260), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.graphimage)
        # ALL LABELS USED:
        # Making the graph image a label
        self.graph_lbl = ttk.Label(self, image=self.photo)
        # Title of Page
        self.infotitle = ttk.Label(self, text="  Information  ",
                                   font=('Mangabey', 50, 'underline'))
        # Subtitle of Page
        self.notetitle = ttk.Label(self, text=" Note:  ",
                                   font=('Clip', 20, 'underline'))
        self.notetext = ttk.Label(
            self,
            text="""Early Breaks will not be saved into the data
as they are not considered 'Completed Study'""",
            font=('Cambria Bold', '12'))
        # Subtitle2
        self.usefulinfotitle = ttk.Label(self, text=" Useful Information:  ",
                                         font=('Clip', 20, 'underline'))
        self.infofact1 = ttk.Label(
            self,
            text="""• Consistent Study Periods
improve your study effectiveness""",
            font=('Cambria Bold', '14'))
        self.infofact2 = ttk.Label(
            self,
            text="""• Too long study sessions are
not as effective in completing work""",
            font=('Cambria Bold', '14'))
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic",
                                font=("impact", 8))
        # ALL LABELS PLACED IN (X, Y) CO-ORDINATES:
        self.notetext.place(x=380, y=155)
        self.graph_lbl.place(x=30, y=105)
        self.infotitle.place(x=225, y=0)
        self.notetitle.place(x=380, y=120)
        self.usefulinfotitle.place(x=380, y=210)
        self.infofact1.place(x=385, y=240)
        self.infofact2.place(x=385, y=290)
        self.footer.place(x=0, y=451)
        # Main Menu Button
        self.buttonMain = tk.Button(self, text="Main Menu", font=('Clip', 22),
                                    command=lambda: self.change_page(0))
        # Placing the button
        self.buttonMain.place(x=240, y=380, width=260, height=60)
