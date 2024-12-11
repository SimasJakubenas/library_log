from classes.admin import Admin
from classes.book import Book
from constants import *


def main_menu_controls(user, library_initiation):
    while True:
        sub_choice = input("Enter your choice: ")
        
        if sub_choice == "1":
            print("All books:")
            # Show all books
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
        book_title = input("Enter book title: ")
        strippped_title = book_title.strip()
        
        if len(book_title) == 0:
            print("Title cannot be empty!")
            continue
        
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
            return genre
        
        else:
            print("Invalid genre!")
            continue


def quantity_validation():
    while True:
        
        try:
            quantity = int(input("Enter book quantity (1-10): "))
        
            if quantity < 1 or quantity > 10:
                print("Quantity must be between 1 and 10!")
                continue
            
            else:
                return quantity
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue