from modules.authentication import register, login
from modules.main_menu import main_menu_controls
from modules.create_admin import create_admin
from classes.colors import Bcolors
from classes.library import Library
from classes.terminal_positioning import Positioning
from views.authentication_menu import authentication_menu
from views.main_menu import main_menu_view
from views.welcome_message import welcome_message
from utility.clear import clear
from constants import *


def main():
    library_initiation = Library()
    line_position = Positioning()
    
    create_admin()
    
    while True:
        if line_position.empty_line == True:
            print("")

        welcome_message()
        authentication_menu()
        choice = input("Enter your choice:\n>>> ")
        line_position.empty_line = True
        clear()
        
        if choice == "1":
            line_position.empty_line = True
            user = register(library_initiation, line_position)
            
            if user is not None:
                line_position.empty_line = False
                main_menu_view(user, line_position)
                main_menu_controls(user, library_initiation, line_position)
            
        elif choice == "2":
            user = login(library_initiation, line_position)
            
            if user is not None:
                line_position.empty_line = False
                main_menu_view(user, line_position)
                main_menu_controls(user, library_initiation, line_position)
        
        elif choice == "0":
            exit()
        
        else:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Invalid choice!{Bcolors.ENDC}")

if __name__ == "__main__":
    main()