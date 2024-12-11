import pickle
from classes.admin import Admin
from classes.book import Book
from constants import *


def main_menu_controls(user, library_initiation):
    while True:
        sub_choice = input("Enter your choice: ")
        
        if sub_choice == "1": # Show all books
            print("-" * 80)
            print(f"Title" + " " * 25 + "| Author" + " " * 12 + "| Year| Genre" + " " * 12 + "| No|")
            print("-" * 80)
            
            with open(BOOK_LOG_PATH, "rb") as book_log:
                book_list = pickle.load(book_log)
                
            if len(book_list) == 0:
                print("No books in the library.")
            
            elif len(book_list) <= 5:
                for book_instance in book_list:
                    print(book_instance)
            
            else:
                for i in range(5):
                    print(book_list[i])
                    print("-" * 80)
                print(f"And {len(book_list) - 5} more...")
            
        elif sub_choice == "2":
            print("Overdue books:")
            # Show overdue books
        elif sub_choice == "3":
            book_title = input("Enter book title: ")
            # Search for book
        elif sub_choice == "4": # Add new book
            if isinstance(user, Admin):
                print("Add a book to library\n")
                
                book_title = title_validation()
                author = author_validation()
                publication_year = publication_year_validation()
                genre = genre_validation()
                quantity = quantity_validation()
                    
                book = Book(book_title, author, publication_year, genre, quantity)
                library_initiation.add_book(book)

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


def title_validation():
    while True:
        book_title = input("Enter book title (You only have 32 characters): ")
        strippped_title = book_title.strip()
        
        if len(book_title) == 0:
            print("Title cannot be empty!")
            continue
        
        elif len(book_title) > 30:
            book_title = book_title[:31]
        
        if len(strippped_title.strip()) == 0:
            print("Title cannot contain only special symbols")
            continue
        
        return book_title


def author_validation():
    while True:
        author = input("Enter book author: ")
        strippped_author = author.strip()
        
        if len(author) == 0:
            print("Author cannot be empty!")
            continue
        
        elif len(author) > 18:
            author = author.split()[-1]
            
            if len(author) > 18:
                author = author[:19]
        
        if len(strippped_author.strip()) == 0:
            print("Author cannot contain only special symbols")
            continue
        
        return author


def publication_year_validation():
    while True:
        
        try:
            publication_year = int(input("Enter book publication year (yyyy): "))
            
            if publication_year < 1900 or publication_year > 2100:
                print("Invalid publication year!")
                continue
            
            else:
                return publication_year
            
        except ValueError:
            print("Invalid input! Please enter a valid year.")
            continue


def genre_validation():
    while True:
        print(BOOK_GENRES)
        genre = input("Enter book genre from the list: ")
        genre_names_lower = []
        
        for genre_name in BOOK_GENRES:
            genre_names_lower.append(genre_name.lower())
        
        if genre.lower() in genre_names_lower:
            return genre.title()
        
        else:
            print("Invalid genre!")
            continue


def quantity_validation():
    while True:
        
        try:
            quantity = int(input("Enter book quantity (1-8): "))
        
            if quantity < 1 or quantity > 8:
                print("Quantity must be between 1 and 8!")
                continue
            
            else:
                return quantity
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue