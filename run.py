from password_generator import PasswordGenerator
import random
from credentials import Users

pwo = PasswordGenerator()
pwo.generate()
pwo.minlen = 6
pwo.maxlen = 12 
class User :
    def __init__(self,name,generate,username,password,length):
					self.name = name
					self.username = username
					self.generate = generate
					self.password = password
					self.length = length

print("Would you want to use this suggested password? " +'\n' "Type 'Yes' or 'No'" ) 

chosen_element= input()
if str(chosen_element) == 'Yes':
	print( User.name + " your username is " + User.username + " and your password is: " +  User.generate)
elif str(chosen_element) == 'No':
	password = input("Enter in your password: " )
	if len(password) < pwo.minlen:
		print('Invalid password, password must atleast contain six characters') 
		length= int(len(password))
		print("Your password coglobal users_list ntains: " + str(length) + " characters " + '\n') 
		print("Type another password")
		password = input("Enter in your password: " )
	else: 
		print(User.username + " your have successfully signed up.")
		print(User.name + " your username is " + User.username + " and your password is: " + password) 

