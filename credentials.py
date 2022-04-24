import unittest
from ast import If, IfExp
from password_generator import PasswordGenerator
pwo = PasswordGenerator()

name = input("Enter Your Username: ")
# if len(name) > 3:
#    print('Valid username') 
# else:
#     print('Invalid username')  

suggested = (pwo.generate())
display =print("Suggested password: " + suggested) 
password = input("Enter in your password: " )
length= int(len(password))
print("Your password contains: " + str(length) + " characters")

if len(password) > 6:
   print('Valid password') 
else:
    print('Invalid password, password must atleast contain six characters')   


f = open('user.txt', 'w')
# f.write(“Hello Python \n”)
f.write("Account Details \n")
f.write("Username: " + name + '\n')
f.write("Password: " + password + '\n') 
#in the above code ‘\n’ is next line which means in the text file it will write Hello Python and point the cursor to the next line

 
class credentials: 
    def __init__(self, username,password) -> None:
        self.username = username
        self.password = password
