import unittest
import update

class TestAppointment(unittest.TestCase):
    def search_db(self):
        
        self.assertEqual(self.input, self.namenet.get() )
        self.assertEqual(self.res, c.execute(sql, (self.input,)) )

    def update_db(self):
        
        self.assertEqual(c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),)), tkinter.messagebox.showinfo("Yayy", "Successfully Updated!") )
    
    def delete_db(self):
        self.assertEqual(c.execute(sql2, (self.namenet.get(),)), tkinter.messagebox.showinfo("Yayy", "Successfully Deleted!"))

if __name__ == '__main__':
    unittest.main()