from modules.authentication import register, login
from modules.main_menu import main_menu_controls
from classes.admin import Admin
from views.authentication_menu import authentication_menu
from views.main_menu import main_menu_view

def main():
    print("Welcome to the Library Management System!")
    
    while True:
        authentication_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user = register()
            main_menu_view(user)
            main_menu_controls(user)
            
        elif choice == "2":
            user = login()
            main_menu_view(user)
            main_menu_controls(user)
        
        elif choice == "0":
            exit()
        
        else:
            print("Invalid choice!")

main()