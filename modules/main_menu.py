import pickle
import os
from classes.admin import Admin
from classes.book import Book
from classes.terminal_positioning import Positioning
from views.book_table_top import book_table_top
from views.main_menu import main_menu_view
from views.adding_book import add_book_view
from utility.clear import clear
from constants import *


def main_menu_controls(user, library_initiation, line_position):
    while True:
        sub_choice = input("Enter your choice: ")
        
        if sub_choice == "1": # Show all books
            book_log_functionality(user, line_position)
            
        elif sub_choice == "2":
            print("Overdue books:")
            # Show overdue books
        elif sub_choice == "3":
            book_title = input("Enter book title: ")
            # Search for book
        elif sub_choice == "4": # Add new book
            if isinstance(user, Admin):
                clear()
                
                book_title = title_validation(line_position)
                author = author_validation(line_position)
                publication_year = publication_year_validation(line_position)
                genre = genre_validation(line_position)
                quantity = quantity_validation(line_position)
                    
                book = Book(book_title, author, publication_year, genre, quantity)
                library_initiation.add_book(book)
                
                print(f"'{book.title}' added to library")
                main_menu_view(user, line_position)

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


def title_validation(line_position):
    while True:
        add_book_view(line_position)
        
        book_title = input("Enter book title (You only have 32 characters): ")
        clear()
        strippped_title = book_title.strip()
        
        if len(book_title) == 0:
            line_position.empty_line = False
            print("Title cannot be empty!")
            continue
        
        elif len(book_title) > 30:
            book_title = book_title[:31]
        
        if len(strippped_title.strip()) == 0:
            line_position.empty_line = False
            print("Title cannot contain only special symbols")
            continue
        
        line_position.empty_line = True
        
        return book_title


def author_validation(line_position):
    while True:
        add_book_view(line_position)
        author = input("Enter book author: ")
        clear()
        strippped_author = author.strip()
        
        if len(author) == 0:
            line_position.empty_line = False
            print("Author cannot be empty!")
            continue
        
        elif len(author) > 18:
            author = author.split()[-1]
            
            if len(author) > 18:
                author = author[:19]
        
        if len(strippped_author.strip()) == 0:
            line_position.empty_line = False
            print("Author cannot contain only special symbols")
            continue
        
        line_position.empty_line = True
        
        return author


def publication_year_validation(line_position):
    while True:
        add_book_view(line_position)
        
        try:
            publication_year = int(input("Enter book publication year (yyyy): "))
            clear()
            
            if publication_year < 1900 or publication_year > 2100:
                line_position.empty_line = False
                print("Invalid publication year!")
                continue
            
            else:
                line_position.empty_line = True
                return publication_year
            
        except ValueError:
            clear()
            line_position.empty_line = False
            print("Invalid input! Please enter a valid year.")
            continue


def genre_validation(line_position):
    while True:
        add_book_view(line_position)
        genre_display_split = split_list(BOOK_GENRES, BOOK_GENRES_SPLIT)
        
        # Determine the maximum width for each column
        col_widths = [max(len(str(item)) for item in col) for col in zip(*genre_display_split)]

        # Create a format string based on column widths
        format_str = ' | '.join(f'{{:<{width}}}' for width in col_widths)

        # Print the table
        for row in genre_display_split:
            print(format_str.format(*row))
            
        genre = input("\nEnter book genre from the list: ")
        clear()
        genre_names_lower = []
        
        for genre_name in BOOK_GENRES:
            genre_names_lower.append(genre_name.lower())
        
        if genre.lower() in genre_names_lower:
            line_position.empty_line = True
            return genre.title()
        
        else:
            line_position.empty_line = False
            print("Invalid genre!")
            continue


def quantity_validation(line_position):
    while True:
        add_book_view(line_position)
        try:
            quantity = int(input("Enter book quantity (1-8): "))
            clear()
        
            if quantity < 1 or quantity > 8:
                line_position.empty_line = False
                print("Quantity must be between 1 and 8!")
                continue
            
            else:
                line_position.empty_line = True
                return quantity
        
        except ValueError:
            clear()
            line_position.empty_line = False
            print("Invalid input! Please enter a valid number.")
            continue


def split_list(lst: list, interval: int):
    """Creates a list of nested lists which length is based on the interval

    Args:
        lst (list): any list
        interval (int): any positive digit that is less than the length of lst

    Returns:
        list: nested lists of lists
    """
    return [lst[i:i + interval] for i in range(0, len(lst), interval)]


def book_log_functionality(user, line_position):
    clear()
    
    with open(BOOK_LOG_PATH, "rb") as book_log:
        book_list = pickle.load(book_log)
        
    if len(book_list) == 0:
        clear()
        print("No books in the library.")
        main_menu_view(user, line_position)
        return
    
    elif len(book_list) <= 5:         
        if line_position.empty_line == True:
            print("")
            
        book_table_top()
        
        for book_instance in book_list:
            print(book_instance)
        
        print("-" * 80)
        print(f"\nPage 1/1\n")
        
    else:
        book_log_pagination(user, line_position, book_list)


def book_log_menu(current_page, number_of_pages):
    print("-" * 80)
    print(f"\nPage {current_page+1}/{number_of_pages}\n")
    
    if current_page == 0:
        print(" " * 6 + "| 1. Next page |" + " " * 18 + "| 3. Last page" + " | 0. Back to Menu |" + " " * 6)
    
    elif current_page == number_of_pages - 1:
        print(" " * 20 + " | 2. Previous page |" + " " * 14 + "| 0. Back to Menu |" + " " * 6)
    
    else:
        print(" " * 6 + "| 1. Next page | 2. Previous page | 3. Last page | 0. Back to Menu |" + " " * 6)


def book_log_controls(user, page_choice, current_page, number_of_pages, line_position):
    if page_choice == "1" and current_page != number_of_pages - 1:
        current_page += 1
        line_position.empty_line = True
        clear()
        
        return current_page
    
    elif page_choice == "2" and current_page != 0:
        current_page -= 1
        line_position.empty_line = True
        clear()
        
        return current_page
    
    elif page_choice == "3" and current_page != number_of_pages - 1:
        current_page = number_of_pages - 1
        line_position.empty_line = True
        clear()
        
        return current_page
    
    elif page_choice == "0":
        line_position.empty_line = True
        clear()
        main_menu_view(user, line_position)
        current_page = -1
        
        return current_page
    
    else:
        clear()
        print("Invalid choice!")
        line_position.empty_line = False
        
        return current_page


def book_log_pagination(user, line_position, book_list):
    pagination_split = split_list(book_list, PAGINATION)
    number_of_pages = len(pagination_split)
    current_page = 0
    
    while True:
        if line_position.empty_line == True:
            print("")
            
        book_table_top()
        
        for book_instance in pagination_split[current_page]:
            print(book_instance)
        
        if len(pagination_split[current_page]) < 6:
            for x in range(1, 6 - len(pagination_split[current_page])):
                print("")
        
        book_log_menu(current_page, number_of_pages)
        
        page_choice = input("\n>>> Enter your choice: ")
        
        current_page = book_log_controls(
            user, page_choice, current_page, number_of_pages, line_position
            )
        
        if current_page == -1:
            current_page = 0
            break