import getpass
import os
from dotenv import load_dotenv
from utility.clear import clear
from classes.colors import Bcolors
from classes.admin import Admin, User
from views.account_creation import account_creation_view
from views.welcome_message import welcome_message


def username_validation(library_initiation, line_position):
    while True:
        account_creation_view(line_position)
        username = input("Enter your username:\n>>> ")
        clear()
        
        # Load variables from .env file
        load_dotenv()
        
        user_list = os.getenv("USER_CARD_ID_LIST").split(",")
        user_list = [user.strip() for user in user_list]
        
        if username not in user_list:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}User card ID not found. Please check your entry{Bcolors.ENDC}")
            continue
        
        if not username.isalnum():
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Username can only contain alphanumeric characters{Bcolors.ENDC}")
            continue
        
        if len(username) < 6:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Username must be at least 6 characters long{Bcolors.ENDC}")
            continue
        
        elif len(username) > 20:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Username must be no more than 20 characters long{Bcolors.ENDC}")
            continue
        
        line_position.empty_line = True
        
        return username

def password_validation(line_position):
    while True:
        account_creation_view(line_position)
        password = getpass.getpass('Enter your password:\n>>> ')
        clear()
        
        if len(password) < 8:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must be at least 8 characters long{Bcolors.ENDC}")
            continue
        
        elif len(password) > 20:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must be no more than 20 characters long{Bcolors.ENDC}")
            continue

        if not any(char.isdigit() for char in password):
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must contain at least one digit{Bcolors.ENDC}")
            continue
            
        if not any(char.isalpha() for char in password):
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must contain at least one letter{Bcolors.ENDC}")
            continue
            
        if not any(char.isupper() for char in password):
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must contain at least one uppercase letter{Bcolors.ENDC}")
            continue
            
        if not any(char.islower() for char in password):
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Password must contain at least one lowercase letter{Bcolors.ENDC}")
            continue
        
        line_position.empty_line = True
        
        return password
       
def register(library_initiation, line_position):
    username = username_validation(library_initiation, line_position)
    password = password_validation(line_position)
    
    while True:
        account_creation_view(line_position)
        confirm_password = getpass.getpass('Confirm your password:\n>>> ')
        clear()
        
        if password!= confirm_password:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Passwords do not match{Bcolors.ENDC}")
            continue
            
        break
    
    user = library_initiation.add_user(username, password, line_position)
    
    return user

def login(library_initiation, line_position):
    
    for x in range(0, 3):
        if line_position.empty_line == True:
            print("")
            
        welcome_message()
        username = input("Enter your username:\n>>> ")
        password = getpass.getpass('\nEnter your password:\n>>> ')
        clear()
            
        user = library_initiation.authenticate_user(username, password, line_position)
        line_position.empty_line = False

        if isinstance(user,User):
            
            return user

    return None
        