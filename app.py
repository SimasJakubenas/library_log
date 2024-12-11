import getpass
from classes.library import Library


def username_validation(library_initiation):
    while True:
        username = input("Enter your username: ")
        
        if not username.isalnum():
            print("Username can only contain alphanumeric characters.")
            continue
        
        if len(username) < 6:
            print("Username must be at least 6 characters long.")
            continue
        
        elif len(username) > 20:
            print("Username must be no more than 20 characters long.")
            continue
        
        for user_instance in library_initiation.user_list:
            if user_instance.username == username:
                print("Username already exists. Please choose a different one.")
                continue
        
        return username


def password_validation():
    while True:
        password = getpass.getpass('Enter your password: ')
        
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        
        elif len(password) > 20:
            print("Password must be no more than 20 characters long.")
            continue

        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
            continue
            
        if not any(char.isalpha() for char in password):
            print("Password must contain at least one letter.")
            continue
            
        if not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
            continue
            
        if not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter.")
            continue

        return password
        
        
def register():
    library_initiation = Library()
    username = username_validation(library_initiation)
    password = password_validation()
    
    while True:
        confirm_password = getpass.getpass('Confirm your password: ')
        
        if password!= confirm_password:
            print("Passwords do not match.")
            continue
            
        break
    
    library_initiation.add_user(username, password)

register()
