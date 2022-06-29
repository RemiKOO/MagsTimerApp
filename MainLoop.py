import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from threading import Thread
import datetime
import time


# importing files
import HomePage
import Breakpage
import Informationpage
import PreInformationpage
import PreStudypage
import Studypage


class App(ttk.Frame):
    def __init__(self, parent):
        self.exit_study_timer = False
        self.exit_break_timer = False
        ttk.Frame.__init__(self)
        # All files/pages formed into a list
        self.availablePages = [
            HomePage.homepage,
            Studypage.study_page,
            Breakpage.break_page,
            PreInformationpage.Pre_information_page,
            PreStudypage.pre_study_page,
            Informationpage.information_page]
        # Displays Home Page (Index 0 of list) at start up
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.availablePages[0].create(self)

    # The Function used to change between pages
    def change_page(self, nmbr):
        self.exit_study_timer = True
        self.exit_break_timer = True
        # Remove all previous widgets
        for widget in self.winfo_children():
            widget.destroy()
        # Run and create function for the new page
        self.availablePages[nmbr].create(self)

    # Function to quit the app
    def exitapp(self):
        root.quit()

    # Function to locate images
    def make_images(self, imagelocation):
        self.imgtemp = []
        for i in imagelocation:
            self.imgtemp.append(ImageTk.PhotoImage(
                Image.open("./img/"+i+".png")))
        return self.imgtemp

    def submit(self):
        self.timerseconds = int(self.studyminuteinput.get()) * 60
        self.breaktimerseconds = int(self.breakminuteinput.get()) * 60
        self.change_page(1)

    def study_timer(self):
        self.wantedtime = datetime.datetime.now() + datetime.timedelta(0,
                                                                       int(self.timerseconds))

        def timer():
            while True:
                self.timer = float(time.mktime(self.wantedtime.timetuple(
                )) - time.mktime(datetime.datetime.now().timetuple()))
                self.timerS = self.timer % 60
                self.timerM = (self.timer-self.timerS) / 60
                print("Study timer - ", self.timerM, self.timerS)

                if(int(self.timerM) < 10):
                    self.timerMStr = "0" + str(int(self.timerM))
                else:
                    self.timerMStr = str(int(self.timerM))

                if(int(self.timerS) < 10):
                    self.timerSStr = "0" + str(int(self.timerS))
                else:
                    self.timerSStr = str(int(self.timerS))

                self.counterVar.set(self.timerMStr + " : " + self.timerSStr)
                if self.exit_study_timer == False:
                    if datetime.datetime.now() > self.wantedtime:
                        self.change_page(2)
                        break
                elif self.exit_study_timer == True:
                    break
        self.t1 = Thread(target=timer)
        self.t1.start()

    def break_timer(self):
        self.breaktime = datetime.datetime.now() + datetime.timedelta(0,
                                                                      int(self.breaktimerseconds))

        def breaktimer():
            while True:
                self.breaktimer = float(time.mktime(
                    self.breaktime.timetuple()) - time.mktime(datetime.datetime.now().timetuple()))
                self.breaktimerS = self.breaktimer % 60
                self.breaktimerM = (self.breaktimer - self.breaktimerS) / 60
                print("Break timer - ", self.breaktimerM, self.breaktimerS)
                self.breakcounterVar.set(
                    str(int(self.breaktimerM)) + ":" + str(int(self.breaktimerS)))
                if self.exit_break_timer == False:
                    if datetime.datetime.now() > self.wantedtime:
                        self.change_page(2)
                        break
                elif self.exit_break_timer == True:
                    break
        self.t2 = Thread(target=breaktimer)
        self.t2.start()


# Function for Light/Dark Mode Switch + Theme change
def switch_upd():
    global is_darkTheme
    if is_darkTheme:
        root.tk.call("set_theme", "light")  # make it light mode
        is_darkTheme = not is_darkTheme
        # Change Image to Red switch
        night_switch.config(image=switch_off, activebackground='white')
    else:
        root.tk.call("set_theme", "dark")  # make it dark mode
        is_darkTheme = not is_darkTheme
        # Change Image to Green Switch
        night_switch.config(image=switch_on, activebackground='gray')


is_darkTheme = True  # Setting initial theme of GUI
if __name__ == "__main__":
    # Setting up GUI
    root = tk.Tk()
    root.resizable(False, False)  # Prevent resizing of window
    root.title("Student Timer")  # Window Title
    # Add the azure theme for dark/light modes
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")  # set as dark mode
    root.geometry('724x476')  # Window size
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)
    # Setting up Light/Dark Mode Switch + Text
    switch_on = tk.PhotoImage(file="./img/Switch_on.png")
    switch_off = tk.PhotoImage(file="./img/Switch_off.png")
    night_switch = tk.Button(root, image=switch_on,
                             relief='flat', command=lambda: switch_upd())
    Night_Mode = ttk.Label(root, text="Night Mode:", font=('Impact', 10))
    # Placing Light/Dark Mode Switch + Text
    night_switch.place(x=238, y=448)
    Night_Mode.place(x=170, y=450)
    root.mainloop()  # Run the GUI
