from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('C:/Users/Raj/Desktop/Hospital Management System/database.db')
c = conn.cursor()

class Application:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.heading = Label(arg1, text="Update Appointments",  fg='Black', font=('arial 35 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(arg1, text="Enter Patient's Name", font=('arial 15'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(arg1, width=30)
        self.namenet.place(x=280, y=62)

        self.search = Button(arg1, text="Search", width=12, height=1, bg='lightgreen', command=self.search_db)
        self.search.place(x=350, y=102)
    def search_db(self):
        self.input = self.namenet.get()

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        self.uname = Label(self.arg1, text="Name of the Patient", font=('arial 15'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.arg1, text="Age", font=('arial 15'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.arg1, text="Gender", font=('arial 15'))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.arg1, text="Location", font=('arial 15'))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.arg1, text="Time", font=('arial 15'))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.arg1, text="Contact", font=('arial 15'))
        self.uphone.place(x=0, y=340)

        self.ent1 = Entry(self.arg1, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.arg1, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.arg1, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.arg1, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.arg1, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.arg1, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        self.update = Button(self.arg1, text="Update", width=20, height=2, bg='blue', command=self.update_db)
        self.update.place(x=400, y=380)

        self.delete = Button(self.arg1, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        self.var1 = self.ent1.get()
        self.var2 = self.ent2.get()
        self.var3 = self.ent3.get()
        self.var4 = self.ent4.get()
        self.var5 = self.ent5.get()
        self.var6 = self.ent6.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Yayy", "Successfully Updated!")
    def delete_db(self):
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Yayy", "Successfully Deleted!")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()