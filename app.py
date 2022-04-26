import string
from random import *

user = ""

class Password:
    def __init__(self, length):
        self.length = length

    def generate(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for x in range(0, self.length))
        return password


class Credentials:
    def __init__(self, username, password):
        self.username = username.strip()
        self.password = password.strip()

    def add_credentials(self):
        with open("user.txt", "a") as credentials:
            credentials.writelines("\n{username}, {password}".format(
                username=self.username, password=self.password))


class User:

    def __init__(self, username, password):
        self.username = username.strip()
        self.password = password.strip()

    def signup(self):
        print("User successfully created")
        print("Adding to database....")
        credentials = Credentials(self.username, self.password)
        credentials.add_credentials()

"""
The method below takes in username from the user, generates
a password and recommends it to them. If they do not want
the generated password, they can entered their own desired password
"""
def create_user():
    print('\nTo signup, enter a username and password:')
    username = input("Enter a username: ")

    password = Password(8)
    generated_password = password.generate()

    use_gen_pass = str(input(
        "\nWould you like to use this password: '{}'\? (Y/n)".format(generated_password)))
    if use_gen_pass.strip().lower() == "y":
        user = User(username, generated_password)
    else:
        password = input("\nEnter a password: ")
        while len(password.strip()) < 6:
            print("\nPlease make sure your password is atleast 6 characters.")
            password = input("Enter a password: ")

        user = User(username, password)

    user.signup()

"""
This method searches the user.txt db and checks if the
entered value exists. If it does the user is logged in
if not, the user is prompted to a create an account
"""
def login_user():
    print('\nTo login, enter your account details:')
    username = input("Enter username: ")
    password = input("Enter password: ")

    passed_in_credentials = "{username}, {password}".format(
        username=username, password=password)
    passed_in_credentials_alt = "{}\n".format(passed_in_credentials)

    with open("user.txt", "r") as f:
        for DB_credentials in f:
            if DB_credentials == passed_in_credentials or DB_credentials == passed_in_credentials_alt:
                return print("Successfully logged in")

        print("\nUser doesn't exist")
        create_user()


"""
The method below opens the db file user.txt and prints out
its contents, in this case the saved credentials
"""
def view_credentials():
    with open("user.txt", "r") as f:
        print("\nThese are all your saved credentials!")
        for DB_credentials in f:
            crendential = DB_credentials.split(",")
        print("Username: {username}, Password: {password}". format(
        username=crendential[0], password=crendential[1]))


def main():
    print('Hello! Welcome to Password Locker.')
    print('Use these codes to navigate: \n 1 ==> Sign Up \n 2 ==> Log In \n 3 ==> Exit \n 4 ==> Show saved credentials')

    short_code = input('\nEnter a choice: ').lower().strip()

    if short_code == '3':
        exit()
    elif short_code == '1':
        create_user()
    elif short_code == '2':
        login_user()
    else:
        view_credentials()


main()