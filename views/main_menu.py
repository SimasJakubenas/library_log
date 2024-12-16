from classes.admin import Admin


def main_menu_view(user, line_position):
    if line_position.empty_line == True:
        print("")
    print("-" * 80)
    print(" " * 25 + "Library's Managing System Menu")
    print("-" * 80)
    print("1. Book search")
    
    if isinstance(user, Admin):
        print("2. Show overdue books")
        print("3. Add new book")
        
    else:
        print("2. My books")

    print("0. Logout\n")
    
