from utility.clear import clear
from classes.admin import Admin
from classes.colors import Bcolors


def update_book_view(user, page_choice, line_position, temp_book_list):
    if line_position.empty_line == True:
        print("")
            
    print("-" * 80)
    print(" " * 31 + "Your selected book")
    print("-" * 80)
    
    for line in range(0, page_choice):
        print("")
    
    try:
        if temp_book_list[page_choice].is_overdue:
            print(f"{Bcolors.FAIL}{page_choice + 1} | {temp_book_list[page_choice]}{Bcolors.ENDC}")
        else:
            print(f"{page_choice + 1} | {temp_book_list[page_choice]} {temp_book_list[page_choice].quantity:<2}|")
    except IndexError:
        clear()
        line_position.empty_line = False
        print("Wrong input")
        
        return False
    
    for line in range(0, 4 - page_choice):
        print("")
        
    print("-" * 80 + "\n\n\n")
    
    if isinstance(user, Admin):
        print(" " * 7 + "| Q. Add book | W. Delete book | E. Remove book | P. Back to Menu |\n")
    else:
        if line_position.my_books_menu == True:
            print(" " * 7 + "| Q. Return book |" + " " * 30 + "| P. Back to Menu |\n")
        else:
            print(" " * 7 + "| Q. Borrow book |" + " " * 30 + "| P. Back to Menu |\n")
    return True