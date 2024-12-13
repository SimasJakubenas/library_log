from utility.clear import clear


def update_book_view(page_choice, line_position, temp_book_list):
    if line_position.empty_line == True:
            print("")
            
    print("-" * 80)
    print(" " * 31 + "Your selected book")
    print("-" * 80)
    
    for line in range(0, page_choice):
        print("")
    
    try:
        print(f"{page_choice + 1} | {temp_book_list[page_choice]}")
    except IndexError:
        clear()
        line_position.empty_line = False
        print("Wrong input")
        
        return False
    
    for line in range(0, 4 - page_choice):
        print("")
        
    print("-" * 80)
    print(" " * 80 + "\n\n")
    print(" " * 7 + "| Q. Add book | W. Delete book | E. Remove book | P. Back to Menu |\n")
    
    return True