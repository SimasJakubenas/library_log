def book_table_top(line_position):
    """
    Prints the table header
    """
    if line_position.empty_line == True:
        print("")
    
    print("-" * 80)
    
    if line_position.my_books_menu == True:
        print(f"# | Title" + " " * 25 + "| Author" + " " * 12 + "| Year| Genre" + " " * 8 + "|Due|")
    
    else:
        print(f"# | Title" + " " * 25 + "| Author" + " " * 12 + "| Year| Genre" + " " * 8 + "| No|")
    print("-" * 80)