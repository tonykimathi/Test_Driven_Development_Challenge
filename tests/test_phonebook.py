import unittest
from app.phonebook import phonebookclass


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.contact = phonebookclass("Name", int(123456))

    def tearDown(self):
        del self.contact

    def test_no_name(self):
        self.assertTrue(self.contact.add_contact(None, None), "Item must have a name")

    def test_invalid_name(self):
        self.assertTrue(self.contact.add_contact([1, 2], None), "Item must have a name")

    def test_phone_book_name_is_str(self):
        self.assertIsInstance(self.contact.name, str)

    def test_phone_number_is_int(self):
        self.assertIsInstance(self.contact.phone_number, int)

    def test_phone_number_is_less_than_six_digits(self):
        self.assertIsInstance(self.contact.phone_number, int)

if __name__ == '__main__':
    unittest.main()
