from classes.admin import Admin

def main_menu_controls(user):
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