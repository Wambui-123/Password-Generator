from password_generator import PasswordGenerator
pwo = PasswordGenerator()
pwo.minlen = 6
pwo.maxlen = 12
pwo.generate()



class User :
    accout_info = []
    
    def __init__(self,username,generate,password,length):
        self.username = username
        self.generate = generate
        self.password = password
        self.length = length
        
        
username = input("Enter Your Username: ")
generate = (pwo.generate())
print("Suggested password: " + generate) 
password = input("Enter in your password: " )
length= int(len(password))
print("Your password contains: " + str(length) + " characters")

if len(password) == pwo.minlen:
   print('Valid password') 
else:
    print('Invalid password, password must atleast contain six characters') 
    
f = open('user.txt', 'w')
f.write("Account Details \n")
f.write("Username: " + username + '\n')
f.write("Password: " + password + '\n')     

