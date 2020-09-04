from tkinter import *
import sqlite3
import pyttsx3

conn = sqlite3.connect('C:/Users/Raj/Desktop/Hospital Management System/database.db')
c = conn.cursor()

number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)

class Application:
    def __init__(self, arg1):
        self.arg1 = arg1

        self.x = 0
        
        self.heading = Label(arg1, text="Show Appointments", font=('arial 50 bold'), fg='black')
        self.heading.place(x=350, y=0)

        self.change = Button(arg1, text="Next Appointment", width=25, height=2, bg='lightgreen', command=self.func)
        self.change.place(x=500, y=600)

        self.n = Label(arg1, text="", font=('arial 180 bold'))
        self.n.place(x=500, y=100)

        self.pname = Label(arg1, text="", font=('arial 50 bold'))
        self.pname.place(x=300, y=400)
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()