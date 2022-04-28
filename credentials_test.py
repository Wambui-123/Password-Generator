import unittest
from app import Credentials



class TestUser(unittest.TestCase):
    '''
    Test class to define test cases for the User class

    Args:
        unittest.TestCase: TestCase class creates test cases
    '''


    def setUp(self):
        '''
        Method to create test cases for the credentials class
        '''
        self.new_credentials = Credentials("Yvonne", "qwerty123")


    def test__init__(self):
        '''
        test to check object instatiation
        '''
        self.assertEqual(self.new_credentials.username, "Yvonne")
        self.assertEqual(self.new_credentials.password, "qwerty123")


    def test_view_credentials(self):
        '''
        method to save credentials
        '''
        self.new_credentials.add_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == "__main__":
    unittest.nain()