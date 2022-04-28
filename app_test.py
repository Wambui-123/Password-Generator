import unittest
from app import User
from app import Credentials

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
        self.new_user = User("Yvonne", "123qwerty")
        self.new_credentials = Credentials("Yvonne", "qwerty123")


def test__init__(self):
            self.assertEqual(self.new_user.username, "Yvonne")
            self.assertEqual(self.new_user.password, "123qwerty")
            
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user = []    
            
def test_save_user(self):
        '''
        to save user object to our user list
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user), 1)   
        

def test_delete_user(self):
        ''' 
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)                         
        
  
if __name__ == '__main__':
    unittest.main()          
            
            
        
            
            
            
            