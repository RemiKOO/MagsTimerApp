from inspect import ismethoddescriptor
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

# Further Information Page
class information_page:
    def create(self):
        self.studygraph(self.datalist)
        self.image = Image.open('./img/graph.png')
        self.graphimage = self.image.resize((380, 260), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.graphimage)
        self.graph_lbl = ttk.Label(self, image=self.photo)
        self.graph_lbl.place(x=30, y=105)
        self.infotitle = ttk.Label(self, text="  Information  ", font=('Mangabey', 50, 'underline'))
        self.infotitle.place(x=225, y=0)
        self.notetitle = ttk.Label(self, text=" Note:  ", font=('Clip', 20, 'underline'))
        self.notetitle.place(x=390, y=110)
        self.notetext = ttk.Label(self, text="Early Breaks are not considered \nCompleted Study Sessions and therefore \nnot included in the users data", font=('Cambria Bold', '12'))
        self.notetext.place(x=390, y=145)
        self.usefulinfotitle = ttk.Label(self, text="  Useful Information  ", font=('Clip', 20, 'underline'))
        self.usefulinfotitle.place(x=420, y=215)
        self.infofact1 = ttk.Label(self, text="• Consistent Study Periods improve \n your study effectiveness", font=('Cambria Bold', '14'))
        self.infofact1.place(x=390, y=255)
        self.infofact2 = ttk.Label(self, text="• Too long study sessions are not \n as effective in completing work", font=('Cambria Bold', '14'))
        self.infofact2.place(x=390, y=305)
        self.buttonMain = tk.Button(self, text="Main Menu", font=('Clip', 22), command=lambda: self.change_page(0))
        self.buttonMain.place(x=240, y=380, width=260, height=60)
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic", font=("impact", 8))
        self.footer.place(x=0, y=451)






