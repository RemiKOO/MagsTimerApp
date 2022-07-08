from inspect import ismethoddescriptor
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

# Further Information Page
class information_page:
    def create(self):
        self.image = Image.open('./img/graph.png')
        self.image = self.image.resize((380, 260), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.graph_lbl = ttk.Label(self, image=self.photo)
        self.graph_lbl.place(x=30, y=95)
        self.label = ttk.Label(self, text="  Information  ", font=('Mangabey', 50, 'underline'))
        self.label.place(x=225, y=0)
        self.label = ttk.Label(self, text="  Useful Information  ", font=('Clip', 20, 'underline'))
        self.label.place(x=420, y=110)
        self.label = ttk.Label(self, text="• Consistent Study Periods improve \n your study effectiveness", font=('Cambria Bold', '14'))
        self.label.place(x=390, y=150)
        self.label = ttk.Label(self, text="• Too long study sessions are not \n as effective in completing work", font=('Cambria Bold', '14'))
        self.label.place(x=390, y=205)
        self.label = ttk.Label(self, text="• Setting consistent Study Periods \n never leads to procrastination", font=('Cambria Bold', '14'))
        self.label.place(x=390, y=260)
        self.label = ttk.Label(self, text="• Overworking leads to progressively \n slower working productivity", font=('Cambria Bold', '14'))
        self.label.place(x=390, y=315)
        self.buttonM = tk.Button(self, text="Main Menu", font=('Clip', 22), command=lambda: self.change_page(0))
        self.buttonM.place(x=240, y=380, width=260, height=60)
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic", font=("impact", 8))
        self.footer.place(x=0, y=451)






