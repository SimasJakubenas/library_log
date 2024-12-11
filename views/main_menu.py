from classes.admin import Admin


def main_menu_view(user):
    print("1. Show all books")
    print("2. Show overdue books")
    print("3. Book search")
    
    if isinstance(user, Admin):
        print("4. Add new book")
        print("5. Remove old book")
    
    else:
        print("4. Borrow book")
        print("5. My books")
    
    print("0. Logout")
    
