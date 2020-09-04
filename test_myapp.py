import unittest
import appointment

class TestAppointment(unittest.TestCase):
    def book_appointment(self):
        self.assertNotEqual(self.val1, '')
        self.assertNotEqual(self.val2, '')
        self.assertNotEqual(self.val3, '')
        self.assertNotEqual(self.val4, '')
        self.assertNotEqual(self.val5, '')
        self.assertNotEqual(self.val6, '')

        self.assertEqual(self.val1, "INSERT INTO 'appointments' (name) VALUES(?)" )
        self.assertEqual(self.val2, "INSERT INTO 'appointments' (age) VALUES(?)" )
        self.assertEqual(self.val2, "INSERT INTO 'appointments' (location) VALUES(?)" )
        self.assertEqual(self.val2, "INSERT INTO 'appointments' (scheduled_time) VALUES(?)" )
        self.assertEqual(self.val2, "INSERT INTO 'appointments' (phone) VALUES(?)" )

if __name__ == '__main__':
    unittest.main()