from password_generator import PasswordGenerator
import random

pwo = PasswordGenerator()
pwo.generate()
pwo.minlen = 6
pwo.maxlen = 12 

class User :
    def __init__(self,name,username,password,length):
        self.name = name
        self.username = username
        self.password = password
        self.length = length
    
name = input("Your name: ")               
username = input("Enter Your Username: ")
generate = (pwo.generate())
print("Suggested password: " + generate)
print("Would you want to use this suggested password? " +'\n' "Type 'Yes' or 'No'" ) 


chosen_element= input()
if str(chosen_element) == 'Yes':
	print(name + " your username is " + username + " and your password is: " + generate)
elif str(chosen_element) == 'No':
	password = input("Enter in your password: " )
	if len(password) < pwo.minlen:
		print('Invalid password, password must atleast contain six characters') 
		length= int(len(password))
		print("Your password contains: " + str(length) + " characters " + '\n') 
		print("Type another password")
		password = input("Enter in your password: " )
	else: 
		print(username + " your have successfully signed up.")
		print(name + " your username is " + username + " and your password is: " + password) 

    