# Date and Time Libraries
import datetime
import time
# Tkinter Libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning
# Import Graphing Library
import matplotlib.pyplot as plt
# Playsound Library: (Version 1.2.2 required)
from playsound import playsound
# Threading Library:
from threading import Thread
# Extra Libraries
from PIL import ImageTk, Image
import os
from string import ascii_letters, digits

# Importing custom files
import HomePage
import Breakpage
import Informationpage
import PreInformationpage
import PreStudypage
import Studypage


# Private Error Exception For Timer False Input
class LimitError(Exception):
    pass

# Private Error Exception For Name False Input
class NameReqError(Exception):
    pass

class NameReqError2(Exception):
    pass


# Creating the Tkinter class
class App(ttk.Frame):
    def __init__(self, parent):
        self.exit_study_timer = False  # Sets exit for study timer to False
        self.exit_break_timer = False  # Sets exit for break timer to False
        self.current_page = 0  # Keeps track of users current page
        ttk.Frame.__init__(self)  # Initialize the Frame
        # All custom files/pages formed into a list indexed chronologically
        self.availablePages = [
            HomePage.homepage,
            Studypage.study_page,
            Breakpage.break_page,
            PreInformationpage.Pre_information_page,
            PreStudypage.pre_study_page,
            Informationpage.information_page]
        # Split class into 3 columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        # Displays Home Page (Index 0 of list) at start up
        self.availablePages[0].create(self)

    # Function to quit the app
    def exit_app(self):
        root.quit()  # Quits the root

    # Function to locate specific images
    def make_images(self, imagelocation):
        self.img_temp = []  # Stores wanted images in a list (Temporary)
        for i in imagelocation:
            # Open and Add wanted image to the temporary list
            self.img_temp.append(ImageTk.PhotoImage(
                Image.open("./img/" + i + ".png")))
        return self.img_temp  # Close the list

        # The 2 Following Def Functions Involve Page Changes:

    # Function used to change between pages
    def change_page(self, nmbr):
        self.exit_study_timer = True  # Sets exit for study timer to True
        self.exit_break_timer = True  # Sets exit for break timer to True
        # Destroy all widgets of current page
        for widget in self.winfo_children():
            widget.destroy()
        # Run the Create function to make the new desired page
        self.current_page = nmbr
        self.availablePages[nmbr].create(self)

    # Function to progress from HomePage to StudyTimer Page (Validate inputs + Change Page)
    def submit(self):
        try:
            self.name = self.nameinput.get()  # Retrieve users name input from Homepage into a variable
            # Retrieve users study minute/s input from Homepage into a variable and convert to seconds
            self.timerseconds = int(self.studyminuteinput.get()) * 60
            # Retrieve users break minute/s input from Homepage into a variable and convert to seconds
            self.breaktimerseconds = int(self.breakminuteinput.get()) * 60
            # Raising Errors for Respective invalid inputs:
            # If User has used anything that are not letters in their Name Input
            if set(self.name).difference(ascii_letters or digits):
                raise NameError("Invalid Name")  # Raise NameError For = 'Invalid Name'
            if len(set(self.name)) <= 2:  # If Name String has less than 3 characters, raise NameReqError
                raise NameReqError("Too Low")  # Raise the NameReqError For = 'Too Low'
            # If Either timers have a 0 or Negative Minute Input
            if self.timerseconds <= 0 or self.breaktimerseconds <= 0:
                raise ValueError("Negative timer or 0")  # Raise the ValueError For = 'Negative Timer or 0'
            # If Either timers have passed the stopwatch limit (Minute inputs of 1000 or over (AKA 60000 Seconds))
            if self.timerseconds >= 60000 or self.breaktimerseconds >= 60000:
                raise LimitError("Timer Limit reached")  # Raise custom LimitError For = 'Limit of Timer reached'
            self.change_page(1)  # Change to the study page if all Errors were passed/inputs are Valid
        # Respective Raised Errors and their warning messages
        except NameError:  # When NameError is raised:
            showwarning(title="Warning", message="Please Enter a NAME using LETTERS only.")
        except NameReqError:
            showwarning(title="Warning", message="Please enter a Name using at least 3 Letters")
        except ValueError:  # When ValueError is raised:
            showwarning(title="Warning", message="Please enter a WHOLE & POSITIVE Time Value.")
        except LimitError:  # When LimitError is raised:
            showwarning(title="Warning", message="Time value is too large, reduce your timer to under 1000 Minutes")

    # Function to call the study timer
    def study_timer(self):
        # Create variable for desired end time finish (E.G: 10-Minute timer from 8pm = 8:10pm)
        self.wantedtime = datetime.datetime.now() + datetime.timedelta(0, int(self.timerseconds))

        def timer():  # Function to begin the study timer
            while True:
                # Creating a variable for the whole study timer
                self.timer = float(time.mktime(self.wantedtime.timetuple(
                )) - time.mktime(datetime.datetime.now().timetuple()))
                self.timerS = self.timer % 60  # Splitting the study timer variable into a seconds variable
                self.timerM = (self.timer - self.timerS) / 60  # Splitting the study timer into a minutes variable
                print("Study timer - ", self.timerM, self.timerS)  # Print current minute and seconds of study timer
                # To stay symmetrical, when minutes are less than 10, a 0 is added in-front (Example: 01:20)
                if int(self.timerM) < 10:
                    self.timerMStr = "0" + str(int(self.timerM))
                else:  # If this is not the case, the timer is displayed as per usual.
                    self.timerMStr = str(int(self.timerM))
                # To stay symmetrical, when seconds are less than 10, a 0 is added in-front (Example: 10:04)
                if int(self.timerS) < 10:
                    self.timerSStr = "0" + str(int(self.timerS))
                else:  # If this is not the case, the timer is displayed as per usual.
                    self.timerSStr = str(int(self.timerS))
                # Formatting the timer to a MINUTES:SECONDS layout
                self.counterVar.set(self.timerMStr + " : " + self.timerSStr)
                # Whilst the function is false, this check will occur:
                if self.exit_study_timer == False:
                    # If the current time has passed the end-time established at the start of the study_timer function:
                    if datetime.datetime.now() > self.wantedtime:
                        self.enterdata(self.timerseconds)  # Call Enter-Data function as study was completed
                        self.change_page(2)  # Change to next page
                        playsound('./alarmsound.mp3')  # Play sound to alert the user they have finished studying
                        break  # Break the timer
                # If at any point, a function creates the exit to be true, the timer will break.
                elif self.exit_study_timer == True:
                    break
        # Begin a thread in order to run the timer and call other functions at the same time such as change pages
        self.t1 = Thread(target=timer)  # Set target so that it stops after being reached
        self.t1.start()  # Start the thread

    # Function to call the break timer
    def break_timer(self):
        # Create variable for desired end time finish (E.G: 10-Minute timer from 8pm = 8:10pm)
        self.breaktime = datetime.datetime.now() + datetime.timedelta(0, int(self.breaktimerseconds))

        def breaktimer():  # Function to begin the break timer
            while True:
                # Creating a variable for the whole break timer
                self.breaktimer = float(time.mktime(
                    self.breaktime.timetuple()) - time.mktime(datetime.datetime.now().timetuple()))
                self.breaktimerS = self.breaktimer % 60  # Splitting the break timer variable into a seconds variable
                # Splitting the break timer into a minutes variable
                self.breaktimerM = (self.breaktimer - self.breaktimerS) / 60
                # Print current minute and seconds of break timer
                print("Break timer - ", self.breaktimerM, self.breaktimerS)
                # To stay symmetrical, when minutes are less than 10, a 0 is added in-front (Example: 01:20)
                if int(self.breaktimerM) < 10:
                    self.breaktimerMStr = "0" + str(int(self.breaktimerM))
                else:  # If this is not the case, the timer is displayed as per usual.
                    self.breaktimerMStr = str(int(self.breaktimerM))
                # To stay symmetrical, when seconds are less than 10, a 0 is added in-front (Example: 10:04)
                if int(self.breaktimerS) < 10:
                    self.breaktimerSStr = "0" + str(int(self.breaktimerS))
                else:  # If this is not the case, the timer is displayed as per usual.
                    self.breaktimerSStr = str(int(self.breaktimerS))
                # Formatting the break timer to a MINUTES:SECONDS layout
                self.breakcounterVar.set(self.breaktimerMStr + ":" + self.breaktimerSStr)
                # Whilst the function is false, this check will occur:
                if self.exit_break_timer == False:
                    # If the current time has passed the end-time established at the start of the break_timer function:
                    if datetime.datetime.now() > self.breaktime:
                        self.change_page(4)  # Change to next page
                        playsound('./alarmsound.mp3')  # Play sound to alert the user they have finished their break
                        break
                # If at any point, a function creates the exit to be true, the timer will break.
                elif self.exit_break_timer == True:
                    break
        # Begin a thread in order to run the timer and call other functions at the same time such as change pages
        self.t2 = Thread(target=breaktimer)  # Set target so that it stops after being reached
        self.t2.start()  # Start the thread

    # Function to add time studied to data file (file handling)
    def enterdata(self, timeStudied):
        self.file = open('data.txt', 'a')  # Open a file if one does not already exist
        self.file.write(self.name + ':' + str(timeStudied) + '\n')  # Write the time studied (in format) into the file
        self.file.close()  # Close the file

    # Function to call data of a specific user from the data file
    def getdata(self, username):
        try:
            username = self.nameinput.get()
            # If any special characters or digits are used, raise the NameError
            if set(username).difference(ascii_letters + digits):
                raise NameError("Invalid Name, Letters only")  # Raising the NameError
            if len(set(username)) <= 2:  # If Username String has less than 3 characters, raise NameReqError
                raise NameReqError2("Too Low")  # Raise the NameReqError For = 'Too Low'
            self.datalist = []  # Create a new list for the users data
            self.file = open('data.txt', 'r')  # Open the data file
            for line in self.file:  # For every line in the data file
                line = line.replace('\n', '')  # Replace every new line so that the data is in one line
                if username in line:  # If the name input is present in the data file:
                    self.secsStudied = int(line.split(':')[1])  # Collect the time studied in seconds
                    self.minsStudied = int(round(self.secsStudied / 60))  # Convert into minutes
                    self.datalist.append(self.minsStudied)  # Add total minutes into the new list
            self.file.close()  # Close the file
            if len(self.datalist) == 0:  # If no data is found under the input, raise the IndexError:
                raise IndexError("Invalid User, No Data Found")  # Raising the IndexError
            print("Successfull", self.datalist)  # Show the data on the terminal
            self.change_page(5)  # Change page to information page
        # Respective Raised Errors and their warning messages
        except NameError:  # If NameError is raised
            showwarning(title="Warning", message="User Names are LETTERS only. Please Try Again.")
        except NameReqError2: 
            showwarning(title="Warning", message="Please Enter a name with at least 3 letters")
        except IndexError:  # If IndexError is raised
            showwarning(title="Warning", message="No User found, Note:CASE SENSITIVE! Please Try Again.")

    # Function to create user graphs as images
    def studygraph(self, data):
        self.studysession = []  # Create a new list
        for i in range(len(self.datalist)):  # For every data value in the data-list, add a Study #X
            self.studysession.append("Study #" + str(i + 1))
        if is_darkTheme:  # If the app is in dark theme
            fig = plt.figure(facecolor='#333333')  # Set to dark charcoal color (Hex = 333333)
            ax = fig.add_subplot(111)  # Adding axis to the plot
            plt.ylabel("Minutes of Study", color='white')  # Formatting color and text of Y label
            plt.title("Amount of Time Studied per Session", color='white')  # Formatting color and text of Title
            ax.bar(self.studysession, data, color='white')  # Formatting color and text of bar
            ax.set_facecolor("#333333")  # Set to dark charcoal color (Hex = 333333)
            ax.tick_params(axis='x', colors='#FFFFFF')  # Setting White X axis
            ax.tick_params(axis='y', colors='#FFFFFF')  # Setting white Y axis
            for i in ['top', 'bottom', 'left', 'right']:  # For top, bottom, left, right
                ax.spines[i].set_color('#FFFFFF')  # Setting the graph frame to white
            plt.xticks(fontsize=7)  # Setting the size of X axis labels to 7
            # Formatting color, text, and rotation of X axis labels
            ax.set_xticklabels(self.studysession, rotation=45, color='white')
            fig.savefig("./img/graph.png")  # Save these graph settings as a graph.png image
        else:
            fig = plt.figure()  # Create the figure using default color (Default = White)
            ax = fig.add_subplot(111)  # Adding axis to the plot
            plt.ylabel("Minutes of Study")  # Formatting Y label (Default Colors)
            plt.title("Amount of Time Studied per Session")  # Formatting Title (Default Colors)
            ax.bar(self.studysession, data, color='grey')  # Make the bar graph color grey
            plt.xticks(fontsize=7)  # Setting the size of X axis labels to 7
            # Formatting color, text, and rotation of X axis labels
            ax.set_xticklabels(self.studysession, rotation=45)
            fig.savefig("./img/graph.png")   # Save these graph settings as a graph.png image


# Function for Light/Dark Mode Switch + Theme change
def switch_upd():
    global is_darkTheme, app  # Global recognition for special variables
    if is_darkTheme:  # If app WAS in dark theme before changing
        root.tk.call("set_theme", "light")  # Make the theme light mode
        is_darkTheme = not is_darkTheme  # Set the variable to False
        # Change Image to Red switch
        night_switch.config(image=switch_off, activebackground='white')
    else:  # If the app is in light mode
        root.tk.call("set_theme", "dark")  # Make the theme dark mode
        is_darkTheme = not is_darkTheme  # Set the variable to True
        # Change Image to Green Switch
        night_switch.config(image=switch_on, activebackground='gray')
    if app.current_page == 5:  # If current page is Information page:
        # Refresh the page (To rerun the graph color to also change that from light/dark)
        app.change_page(app.current_page)
    else:  # If not
        pass


is_darkTheme = True  # Setting initial theme of GUI to Dark Mode
if __name__ == "__main__":
    if not os.path.exists("data.txt"):
        file = open("data.txt", "w")
        file.close()
    # Setting up GUI
    root = tk.Tk()
    root.resizable(False, False)  # Prevent resizing of window
    root.title("Student Timer")  # Window Title
    # Add the azure theme for dark/light modes
    root.tk.call("source", "azure.tcl") 
    root.tk.call("set_theme", "dark")  # set as dark mode
    root.geometry('724x476')  # Window size (Consistent as resize is false)
    # Link the App and window we made
    app = App(root)  
    app.pack(fill="both", expand=True)
    # Setting up Light/Dark Mode Switch + Text
    switch_on = tk.PhotoImage(file="./img/Switch_on.png")  # Setting the Green Switch img to on variable
    switch_off = tk.PhotoImage(file="./img/Switch_off.png")  # Setting the Red Switch img to off variable
    # Setting the button with command to Function for light/dark mode switch + theme
    night_switch = tk.Button(root, image=switch_on, relief='flat', command=lambda: switch_upd())  
    # Setting a label to indicate the switch to the user
    Night_Mode = ttk.Label(root, text="Night Mode:", font=('Impact', 10))
    # Placing both the Light/Dark Mode Switch and Text in (X, Y) Co-Ordinate format
    night_switch.place(x=238, y=448)
    Night_Mode.place(x=170, y=450)
    root.mainloop()  # Run the GUI
