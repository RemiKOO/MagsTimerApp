from tkinter import ttk
import tkinter as tk


# Further Information Page
class information_page:
    def create(self):
        self.imgList = self.make_images(["graph"])
        self.graph_lbl = ttk.Label(self, image=self.imgList[0])
        self.graph_lbl.place(x=25, y=10)
        self.label = ttk.Label(self, text="  Information  ", font=('Mangabey', 50, 'underline'))
        self.label.place(x=225, y=0)
        self.buttonM = tk.Button(self, text="Main Menu", font=('Clip', 22), command=lambda: self.change_page(0))
        self.buttonM.place(x=240, y=360, width=260, height=60)
        self.footer = ttk.Label(self, text="© Developed by Luka Jeremic", font=("impact", 8))
        self.footer.place(x=0, y=451)






