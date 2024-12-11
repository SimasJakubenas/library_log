from modules.authentication import register, login
from classes.admin import Admin
from views.authentication_menu import authentication_menu
from views.main_menu import main_menu_view

def main():
    print("Welcome to the Library Management System!")
    
    while True:
        authentication_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
            
        elif choice == "2":
            user = login()
            main_menu_view(user)
            
            while True:
                sub_choice = input("Enter your choice: ")
                
                if sub_choice == "1":
                    print("All books:")
                    # Show all books
                elif sub_choice == "2":
                    print("Overdue books:")
                    # Show overdue books
                elif sub_choice == "3":
                    book_title = input("Enter book title: ")
                    # Search for book
                elif sub_choice == "4":
                    if isinstance(user, Admin):
                        book_title = input("Enter book title: ")
                        # Add new book
                    else:
                        book_title = input("Enter book title: ")
                        # Borrow book
                elif sub_choice == "5":
                    if isinstance(user, Admin):
                        print("My books:")
                        # Show my books
                    else:
                        print("Borrowed books:")
                        # Show borrowed books
                elif sub_choice == "0":
                    break
                else:
                    print("Invalid choice!")
        
        elif choice == "0":
            exit()
        
        else:
            print("Invalid choice!")

main()