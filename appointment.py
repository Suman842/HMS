from tkinter import *
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect('C:/Users/Raj\Desktop/Hospital Management System/database.db')
c = conn.cursor()

ids = []

class MyApp:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.left = Frame(arg1, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(arg1, width=400, height=720, bg='lightgreen')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="XYZ Hospital | Book Your Appointment", font=('arial 30 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)
        self.name = Label(self.left, text="Name of the Patient", font=('arial 15'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

        self.age = Label(self.left, text="Age", font=('arial 15'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        self.gender = Label(self.left, text="Gender", font=('arial 15'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)

        self.location = Label(self.left, text="Location", font=('arial 15'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        self.time = Label(self.left, text="Time", font=('arial 15'), fg='black', bg='lightgreen')       
        self.time.place(x=0, y=260)

        self.phone = Label(self.left, text="Contact", font=('arial 15'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=300)

        self.enter_name = Entry(self.left, width=30)
        self.enter_name.place(x=250, y=100)

        self.enter_age = Entry(self.left, width=30)
        self.enter_age.place(x=250, y=140)

    
        self.enter_gender = Entry(self.left, width=30)
        self.enter_gender.place(x=250, y=180)


        self.enter_location = Entry(self.left, width=30)
        self.enter_location.place(x=250, y=220)


        self.enter_time = Entry(self.left, width=30)
        self.enter_time.place(x=250, y=260)


        self.enter_phone = Entry(self.left, width=30)
        self.enter_phone.place(x=250, y=300)


        self.submit = Button(self.left, text="Book Appointment", width=20, height=2, bg='lightgreen', command=self.book_appointment)

        self.submit.place(x=300, y=340)
    
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        self.logs = Label(self.right, text="Logs", font=('arial 25 bold'), fg='white', bg='lightgreen')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Booked Appointments :  " + str(self.final_id))
    def book_appointment(self):
        self.val1 = self.enter_name.get()
        self.val2 = self.enter_age.get()
        self.val3 = self.enter_gender.get()
        self.val4 = self.enter_location.get()
        self.val5 = self.enter_time.get()
        self.val6 = self.enter_phone.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Oops!!!", "You missed one of the above fields...")
        else:
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Yayy", "Appointment Made for " +str(self.val1))
            

            self.box.insert(END, 'Appointment Booked for ' + str(self.val1) + ' at ' + str(self.val5))

root = Tk()
b = MyApp(root)

root.geometry("1200x720+0+0")

root.resizable(False, False)

root.mainloop()