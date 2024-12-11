from modules.authentication import register, login
from modules.main_menu import main_menu_controls
from classes.book import Book
from classes.library import Library
from views.authentication_menu import authentication_menu
from views.main_menu import main_menu_view


def main():
    print("Welcome to the Library Management System!")
    library_initiation = Library()
    while True:
        authentication_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user = register(library_initiation)
            main_menu_view(user)
            main_menu_controls(user, library_initiation)
            
        elif choice == "2":
            user = login(library_initiation)
            main_menu_view(user)
            main_menu_controls(user, library_initiation)
        
        elif choice == "0":
            exit()
        
        else:
            print("Invalid choice!")

main()