import unittest
from app.phonebook import phonebookclass


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.contact = phonebookclass()

    def tearDown(self):
        del self.contact

    def test_add_contact(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
