from modules.authentication import register, login
from classes.admin import Admin

def main():
    print("Welcome to the Library Management System!")
    
    while True:
        print("1. Register")
        print("2. Login")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
            
        elif choice == "2":
            user = login()
            
            print("1. Show all books")
            print("2. Show overdue books")
            print("3. Book search")
            
            if isinstance(user, Admin):
                print("4. Add new book")
                print("5. Remove old book")
            
            else:
                print("4. Borrow book")
                print("5. My books")
            
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