from classes.admin import Admin


def main_menu_view(user, line_position):
    if line_position.empty_line == True:
        print("")
    print("-" * 80)
    print(" " * 25 + "Library's Managing System Menu")
    print("-" * 80)
    print("1. Show all books")
    print("2. Show overdue books")
    print("3. Book search")
    
    if isinstance(user, Admin):
        print("4. Add new book")
        print("5. Remove old book")
    
    else:
        print("4. Borrow book")
        print("5. My books")
    
    print("0. Logout\n")
    
