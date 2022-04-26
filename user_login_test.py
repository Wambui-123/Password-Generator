import unittest
from user_login import User

class TestUser(unittest.TestCase):
    '''
    Test class to define test cases for the User class
    Args:
        unittest.TestCase: TestCase class creates test cases 
    '''

    def setUp(self):
        '''
        Method run before each test to build a start
        '''
        self.new_user = User("Yvonne", "Muthui", "yvonnewambui28@gmail.com", "123qwerty")

    def test__init__(self):
        '''
        test initialization to test object instantiation
        '''

        self.assertEqual(self.new_user.first_name, "Yvonne")
        self.assertEqual(self.new_user.user_name, "Muthui")
        self.assertEqual(self.new_user.email, "yvonnemuthui28@gmail.com")
        self.assertEqual(self.new_user.password, "123qwerty")


    def tearDown(self):
        '''
        method to clean up the user
        '''
        User.user_list = []


    def test_save_user(self):
        '''
        to save user object to our user_list
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


    def test_delete_user(self):
        '''
        
        test_delete_user to test if we can remove a user from our user_list
        '''
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)