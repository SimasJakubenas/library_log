def book_log_menu_view(line_position, number_of_pages):
    print("-" * 80)
    print(f"\nPage {line_position.current_page+1}/{number_of_pages}\n")
    
    if number_of_pages > 1:
        if line_position.current_page == 0:
            print(" " * 6 + "| Q. Next page |" + " " * 18 + "| E. Last page" + " | P. Back to Search |\n")
        
        elif line_position.current_page == number_of_pages - 1:
            print(" " * 20 + " | W. Previous page |" + " " * 14 + "| P. Back to Search |\n")
        
        else:
            print(" " * 6 + "| Q. Next page | W. Previous page | E. Last page | P. Back to Search |\n")
    
    else:
        print(" " * 55 + "| P. Back to Search |\n")