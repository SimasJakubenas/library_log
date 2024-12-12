from modules.authentication import register, login
from modules.main_menu import main_menu_controls
from modules.create_admin import create_admin
from classes.library import Library
from classes.terminal_positioning import Positioning
from views.authentication_menu import authentication_menu
from views.main_menu import main_menu_view
from utility.clear import clear
from constants import *


def main():
    library_initiation = Library()
    line_position = Positioning()
    
    create_admin()
    
    while True:
        if line_position.empty_line == True:
            print("")
            
        print("\n" + " " * 20 + "Welcome to the Library Management System!\n")
        authentication_menu()
        choice = input(">>> Enter your choice: ")
        
        if choice == "1":
            clear()
            line_position.empty_line = True
            user = register(library_initiation, line_position)
            
            if user is not None:
                main_menu_view(user, line_position)
                main_menu_controls(user, library_initiation, line_position)
            
            else:
                line_position.empty_line = False
                clear()
                print("Registration failed. Please try again.")
            
        elif choice == "2":
            clear()
            line_position.empty_line = True
            user = login(library_initiation, line_position)
            
            if user != None:
                main_menu_view(user, line_position)
                main_menu_controls(user, library_initiation, line_position)
        
        elif choice == "0":
            exit()
        
        else:
            line_position.empty_line = False
            clear()
            print("Invalid choice!")

main()