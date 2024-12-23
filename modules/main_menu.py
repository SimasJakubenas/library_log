import pickle
import datetime as dt
import json
from classes.colors import Bcolors
from classes.admin import Admin
from classes.book import Book
from views.book_table_top import book_table_top
from views.main_menu import main_menu_view
from views.adding_book import add_book_view
from views.update_book import update_book_view
from views.book_log_menu import book_log_menu_view
from utility.clear import clear
from utility.split import split_list
from constants import *

def main_menu_controls(user, library_initiation, line_position):
    while True:
        sub_choice = input("Enter your choice:\n>>> ")
        line_position.my_books_menu = False
        line_position.empty_line = True
        clear()
        
        if sub_choice == "1": # Search for book
            book_search_functionality(user, line_position)
            
        elif sub_choice == "2":
            if isinstance(user, Admin): # Show overdue books as Admin
                show_overdue_admin_view(user,line_position)
     
            else: # Show my books as user
                line_position.my_books_menu = True
                book_log_pagination(user, line_position)
                main_menu_view(user, line_position)
                   
        elif sub_choice == "3" and isinstance(user, Admin): # Add new book
            add_new_book(line_position, library_initiation)
            main_menu_view(user, line_position)
                
        elif sub_choice == "0":
            break
        
        else:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Invalid choice!{Bcolors.ENDC}")
            main_menu_view(user, line_position)

def title_validation(line_position):
    while True:
        add_book_view(line_position)
        
        book_title = input("Enter book title (You only have 32 characters): ")
        clear()
        strippped_title = book_title.strip()
        
        if len(book_title) == 0:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Title cannot be empty!{Bcolors.ENDC}")
            continue
        
        elif len(book_title) > 30:
            book_title = book_title[:30]
        
        if len(strippped_title.strip()) == 0:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Title cannot contain only special symbols{Bcolors.ENDC}")
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
            print(f"{Bcolors.FAIL}Author cannot be empty!{Bcolors.ENDC}")
            continue
        
        elif len(author) > 18:
            author = author.split()[-1]
            
            if len(author) > 18:
                author = author[:19]
        
        if len(strippped_author.strip()) == 0:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Author cannot contain only special symbols{Bcolors.ENDC}")
            continue
        
        line_position.empty_line = True
        
        return author

def publication_year_validation(line_position):
    while True:
        add_book_view(line_position)
        
        try:
            publication_year = int(input("Enter book publication year (yyyy): "))
            clear()
            
            if 0 <= publication_year <= 2024:
                line_position.empty_line = False
                print(f"{Bcolors.FAIL}Invalid publication year!{Bcolors.ENDC}")
                continue
            
            else:
                line_position.empty_line = True
                return publication_year
            
        except ValueError:
            clear()
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Invalid input! Please enter year between 0 and 2024{Bcolors.ENDC}")
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
            print(f"{Bcolors.FAIL}Invalid genre!{Bcolors.ENDC}")
            continue

def quantity_validation(line_position):
    while True:
        add_book_view(line_position)
        try:
            quantity = int(input("Enter book quantity (1-8): "))
            clear()
        
            if quantity < 1 or quantity > 8:
                line_position.empty_line = False
                print(f"{Bcolors.FAIL}Quantity must be between 1 and 8!{Bcolors.ENDC}")
                continue
            
            else:
                line_position.empty_line = True
                return quantity
        
        except ValueError:
            clear()
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Invalid input! Please enter a valid number{Bcolors.ENDC}")
            continue

def book_log_controls(user, page_choice, number_of_pages, line_position, temp_book_list, book_title):
    line_position.empty_line = True
    clear()
    
    if page_choice.lower() == "q" and line_position.current_page != number_of_pages - 1:
        line_position.current_page += 1
    
    elif page_choice.lower() == "w" and line_position.current_page != 0:
        line_position.current_page -= 1
    
    elif page_choice.lower() == "e" and line_position.current_page != number_of_pages - 1:
        line_position.current_page = number_of_pages - 1
    
    elif page_choice.lower() == "p":
        line_position.current_page = -1
    
    elif page_choice.isdigit():
        page_choice = int(page_choice) - 1
        
        if not isinstance(user, Admin) and line_position.my_books_menu != True:
            for book_instance in user.borrowed_books:

                if book_instance.is_overdue:
                    line_position.empty_line = False
                    print(f"{Bcolors.FAIL}You have books that are overdue. Can't borrow new books right now{Bcolors.ENDC}")
                    
                    return None
            
        if 0 <= page_choice < 5:
            update_book_quantity(
                user, page_choice, line_position, temp_book_list, book_title
                )
            
        else:
            print(f"{Bcolors.FAIL}Invalid page number!{Bcolors.ENDC}")
            line_position.empty_line = False
    
    else:
        print(f"{Bcolors.FAIL}Invalid choice!{Bcolors.ENDC}")
        line_position.empty_line = False

def book_log_pagination(user, line_position, book_title=None):
    while True:
        if book_title != None:
            book_list = matching_list_creation(line_position, book_title)

            if book_list == False:
                break
        
        else:
            book_list = user.borrowed_books
    
        pagination_split = split_list(book_list, PAGINATION)
        number_of_pages = len(pagination_split)
        
        temp_book_list = display_borrowed_books(user, line_position, book_title, pagination_split)
        
        if temp_book_list == False:
            break
        
        book_log_menu_view(line_position, number_of_pages)
        page_choice = input("Enter your choice:\n>>> ")
        
        book_log_controls(
            user, page_choice, number_of_pages, line_position, temp_book_list, book_title
            )
        
        if line_position.current_page == -1:
            line_position.current_page = 0
            
            break
        
def book_search_functionality(user, line_position):
    while True:
        
        if line_position.empty_line == True:
            print("")
            
        print("-" * 80)
        print(" " * 32 + "Book Search")
        print("-" * 80 + "\n")
        book_title = input(
            "Enter a word or a phrase or press ENTER to go back.\nOr type 'all' to show all books\n>>> "
            )
        clear()
        
        if len(book_title) != 0:
            book_log_pagination(user, line_position, book_title)
            continue

        else:
            line_position.empty_line = True
            main_menu_view(user, line_position)
            break

def update_book_quantity(user, page_choice, line_position, temp_book_list, book_title):
    while True:
        is_right_selection = update_book_view(user, page_choice, line_position, temp_book_list)
        
        if is_right_selection == False:
            book_log_pagination(user, line_position, book_title)
        
        ammend_book_log_choice = input("Enter your choice:\n>>> ")
        line_position.empty_line = True
        clear()
        
        if ammend_book_log_choice.lower() == 'q': # Adds book
            
            if isinstance(user, Admin):
                add_book(temp_book_list, page_choice, line_position)
                
            else:
                show_book(user, line_position, temp_book_list, page_choice)
                break
                
        elif ammend_book_log_choice.lower() == 'w' and isinstance(user, Admin): # Removes book
            remove_book(temp_book_list, page_choice, line_position)
        
        elif ammend_book_log_choice.lower() == 'e' and isinstance(user, Admin): # Deletes book
            filtered_by_text = delete_book(line_position, page_choice, temp_book_list, book_title)
            
            return filtered_by_text
        
        elif ammend_book_log_choice.lower() == 'p': # Go back to search
            line_position.empty_line = True
            break
        
        else:
            print(f"{Bcolors.FAIL}Invalid choice!{Bcolors.ENDC}")
            line_position.empty_line = False
        
def update_book_counter(counter_changer, temp_book_list, page_choice, line_position):
    selected_book = temp_book_list[page_choice]
    with open(BOOK_LOG_PATH, "rb") as pickle_in:
        book_list = pickle.load(pickle_in)

    selected_book.quantity += counter_changer
    
    for book in book_list:
        if book.title == selected_book.title:
            book.quantity = selected_book.quantity
    
    with open(BOOK_LOG_PATH, "wb") as pickle_out:
        pickle.dump(book_list, pickle_out)
        print(f"{Bcolors.OKGREEN}Book updated successfully{Bcolors.ENDC}")
        line_position.empty_line = False

def add_new_book(line_position, library_initiation):
    book_title = title_validation(line_position)
    author = author_validation(line_position)
    publication_year = publication_year_validation(line_position)
    genre = genre_validation(line_position)
    quantity = quantity_validation(line_position)
        
    book = Book(book_title, author, publication_year, genre, quantity)
    library_initiation.add_book(book)
    
    line_position.empty_line = False
    print(f"{Bcolors.OKGREEN}'{book.title}' added to library{Bcolors.ENDC}")

def show_overdue_admin_view(user,line_position):
    while True:
        with open(USER_LOG_PATH, "rb") as pickle_in:
            all_users = pickle.load(pickle_in)

        only_users = list(filter(lambda x: not isinstance(x, Admin), all_users))
        users_with_overdue = {}
        
        for user_instance in only_users:
            overdue_books = [book.title for book in user_instance.borrowed_books if book.is_overdue]
            users_with_overdue[user_instance.username] = overdue_books
        
        print("\n" + "-" * 80)
        print(" " * 28 + "Users with overdue books")
        print("-" * 80 + "\n")
        
        print(json.dumps(users_with_overdue, indent=4))

        return_to_menu = input("\nPress ENTER to return to main menu:\n>>> ")
        clear()
        
        if return_to_menu == "":
            main_menu_view(user, line_position)
            break
        
        else:
            line_position.empty_line = False
            print(f"{Bcolors.FAIL}Invalid choice!{Bcolors.ENDC}")

def display_borrowed_books(user, line_position, book_title, pagination_split):
    book_table_top(line_position)
    temp_book_list = []
    
    try:
        for i, book_instance in enumerate(pagination_split[line_position.current_page]):
            temp_book_list.append(book_instance)
            
            if book_title == None and book_instance.borrow_time != None:
                overdue_check(user, book_instance, i)

            else:
                print(f"{i+1} | {book_instance} {book_instance.quantity} |")
        
        if len(pagination_split[line_position.current_page]) < 6:
            for x in range(1, 6 - len(pagination_split[line_position.current_page])):
                print("")
                
        return temp_book_list
                
    except Exception:
        clear()
        print(f"{Bcolors.FAIL}You don't have any books, use search option to add books{Bcolors.ENDC}")
        line_position.empty_line = False
        
        return False

def matching_list_creation(line_position, book_title):
    with open(BOOK_LOG_PATH, 'rb') as pickle_in:
        book_list = pickle.load(pickle_in)
            
        if book_title.lower() != "all":
            matching_list = []
            
            for book in book_list:
                if book_title.lower() in book.title.lower():
                    matching_list.append(book)
            
            if len(matching_list) == 0:
                clear()
                line_position.empty_line = False
                print(f"{Bcolors.FAIL}No matching books found{Bcolors.ENDC}")
                
                return False
            
            return matching_list
        
        else:
            return book_list

def add_book(temp_book_list, page_choice, line_position):
    counter_changer = 1
                
    if temp_book_list[page_choice].quantity < 8:
        update_book_counter(counter_changer, temp_book_list, page_choice, line_position)
        
    else:
        print(f"{Bcolors.FAIL}Cannot add book. Max qquantity is 8{Bcolors.ENDC}")
        line_position.empty_line = False

def show_book(user, line_position, temp_book_list, page_choice):
    main_menu_view(user, line_position)
    book_choice = temp_book_list[page_choice]
    
    if line_position.my_books_menu == False:
        line_position.empty_line = False
        updated_book_list = user.borrow_book(book_choice)
        
    else:
        line_position.empty_line = False
        user.return_book(book_choice)

def remove_book(temp_book_list, page_choice, line_position):
    counter_changer = -1
            
    if temp_book_list[page_choice].quantity > 0:
        update_book_counter(counter_changer, temp_book_list, page_choice, line_position)
        
    else:
        print(f"{Bcolors.FAIL}Cannot add book. Max qquantity is 8{Bcolors.ENDC}")
        line_position.empty_line = False

def delete_book(line_position, page_choice, temp_book_list, book_title):
    selected_book = temp_book_list[page_choice]
    
    with open(BOOK_LOG_PATH, "rb") as pickle_in:
        book_list = pickle.load(pickle_in)

    filtered_by_text = list(filter(
        lambda x: x if x.title != selected_book.title else None,
        book_list
        ))
    
    if book_title != 'all':
        filtered_by_text = list(filter(
            lambda x: x if book_title.lower() in x.title.lower() else None,
            filtered_by_text
            ))
        
        with open(BOOK_LOG_PATH, "wb") as pickle_out:
            clear()
            pickle.dump(filtered_by_text, pickle_out)
            print(f"{Bcolors.OKGREEN}Book remuved successfully{Bcolors.ENDC}")
            line_position.empty_line = False
        
        return filtered_by_text
        
    with open(BOOK_LOG_PATH, "wb") as pickle_out:
        clear()
        pickle.dump(filtered_by_text, pickle_out)
        print(f"{Bcolors.OKGREEN}Book remuved successfully{Bcolors.ENDC}")
        line_position.empty_line = False
    
    return filtered_by_text

def overdue_check(user, book_instance, i):
    data = dt.datetime.now()
    time_borrowed = book_instance.borrow_time
    remaining_time = BORROWING_TIME + time_borrowed - (data - dt.datetime(1970,1,1)).total_seconds()
    user.user_update()
    
    if remaining_time < 0:
        book_instance.is_overdue = True
        user.user_update()
    if book_instance.is_overdue == True:
        print(f"{Bcolors.FAIL}{i+1} | {book_instance} x |{Bcolors.ENDC}")
    else:
        print(f"{i+1} | {book_instance} {round(remaining_time):<2}|")
