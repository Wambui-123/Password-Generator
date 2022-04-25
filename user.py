from credentials import Users

def main():
    print(' ')
print('Hello! Welcome to Password Locker.')
# while True:
print('Use these codes to navigate: \n sp-Sign Up \n li-Log In \n ex-Exit')
short_code = input('Enter a choice: ').lower().strip()
if short_code == 'ex': 
    exit()      
elif short_code == 'sp':
			# print('To create a new account:')
                from run import User
                print(" ")
elif short_code == 'li':
			print(' ')
			print('To login, enter your account details:')
user = input('Enter Username - ').strip()
password = str(input('Enter your password - '))
# user_exists = (user, password)     
if user == User.username:
        print(f'Welcome {user}. Please choose an option to continue.')
        print(' ')
else: 
    print(f'You do not have an account' "\n" 'Please Sign Up') 
    print('Use these codes to navigate: \n sp-Sign Up \n li-Log In \n ex-Exit')
# while True:
print("-"*60)
print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
short_code = input('Enter a choice: ').lower().strip()
print("-"*60)
if short_code == 'ex':
    print(" ")
    print(f'Goodbye {user}')

# break
# elif short_code == 'cc':
# print(' ')
# print('Enter your credential details:')
# site_name = input('Enter the site\'s name- ').strip()
# account_name = input('Enter your account\'s name - ').strip()
# while True:
# print(' ')
# print("-"*60)
# print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
# psw_choice = input('Enter an option: ').lower().strip()
# print("-"*60)
# if psw_choice == 'ep':
# 	print(" ")
# 	password = input('Enter your password: ').strip()
# 	break
# elif psw_choice == 'gp':
#     password = generate_password()
# break
# elif psw_choice == 'ex':
# 	break
# 		else:
# 		print('Oops! Wrong option entered. Try again.')
# 		save_credential(create_credential(user_name,site_name,account_name,password))
# 		print(' ')
# 		print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
# 		print(' ')
# 		elif short_code == 'dc':
# 						print(' ')
# if display_credentials(user_name):
#     print('Here is a list of all your credentials')
# print(' ')
# for credential in display_credentials(user_name):
#     print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
#     print(' ')	
# else:
#     print(' ')
#     print("You don't seem to have any credentials saved yet")
#     print(' ')
# elif short_code == 'copy':
# print(' ')
# chosen_site = input('Enter the site name for the credential password to copy: ')
# copy_credential(chosen_site)
# print('')


# 			else: 
# 				print(' ')
# 				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
# 		else:
# 			print("-"*60)
# 			print(' ')
# 			print('Oops! Wrong option entered. Try again.')
				
# else short_code == "":
# print('Oops! Wrong option entered. Try again.')





if __name__ == '__main__':
	main()