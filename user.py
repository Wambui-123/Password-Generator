from collections import UserList
from password_generator import PasswordGenerator
import random

pwo = PasswordGenerator()
pwo.generate()
pwo.minlen = 6
pwo.maxlen = 12 

class User :
    	
    def __init__(self,username,generate,password,length):
        self.username = username
        self.generate = generate
        self.password = password
        self.length = length
               
username = input("Enter Your Username: ")
generate = (pwo.generate())
print("Suggested password: " + generate)
print("Would you want to use this suggested password? " +'\n' "Type 'Yes' or 'No'" ) 


chosen_element= input()
if str(chosen_element) == 'Yes':
    print(username + " your password is: " + generate)
elif str(chosen_element) == 'No':
    password = input("Enter in your password: " )
    if len(password) < pwo.minlen:
        print('Invalid password, password must atleast contain six characters') 
        length= int(len(password))
        print("Your password contains: " + str(length) + " characters " + '\n') 
        print("Type another password")
        password = input("Enter in your password: " )
    else: 
     print(username + " your have successfully logged in.")
    print("Your password is " + password)        
    
    
def main(): 
        f = open('user.txt', 'a')
        f.write("Account Details " + '\n')
        f.write("Username: " + username + '\n')
        f.write("Password: " + password + '\n')  
        f.close()   
        main()    

