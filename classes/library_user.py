import pickle
from classes.colors import Bcolors
from classes.user import User
from utility.clear import clear
from constants import *


class Library_user(User):
    def __init__(self, username, password, have_overdue=False):
        super().__init__(username, password)
        self.have_overdue = have_overdue
        self.borrowed_books = []
        
    def borrow_book(self, book):
        clear()
        
        if len(self.borrowed_books) < 5:

            if book.quantity > 0:
                for book_instance in self.borrowed_books:
                    if book_instance.title == book.title:
                        print(f"{Bcolors.FAIL}You already borrowed '{book.title}{Bcolors.ENDC}")
                        return None
                    
                counter_changer = -1
                self.borrowed_books.append(book)
                updated_books = self.book_update(book, counter_changer)
                self.user_update()
                book.borrowing_time()
                
                
                print(f"{Bcolors.OKGREEN}'{book.title}' has been borrowed{Bcolors.ENDC}")
                
                return updated_books
                
            else:
                print(f"{Bcolors.FAIL}'{book.title}' is currently unavailable{Bcolors.ENDC}")
            
        else:
            clear()
            print(f"{Bcolors.FAIL}You have reached your borrowing limit{Bcolors.ENDC}")

    
    def return_book(self, book):
        clear()
        counter_changer = 1
        self.borrowed_books.remove(book)
        updated_books = self.book_update(book, counter_changer)
        self.user_update()
        book.reset_borrowing_time()

        print(f"{Bcolors.OKGREEN}'{book.title}' has been returned{Bcolors.ENDC}")
        
        return updated_books
    
    def user_update(self):
        with open(USER_LOG_PATH, "rb") as pickle_in:
            all_users = pickle.load(pickle_in)
        
        for user_instance in all_users:
            if user_instance.username == self.username:
                user_instance.borrowed_books = self.borrowed_books
                break
    
        with open(USER_LOG_PATH, "wb") as pickle_out:
            pickle.dump(all_users, pickle_out)
    
    def book_update(self, book, counter_changer):
        with open(BOOK_LOG_PATH, "rb") as pickle_in:
            all_books = pickle.load(pickle_in)
        
        for book_instance in all_books:
            if book_instance.title == book.title:
                book_instance.quantity += counter_changer
                break
        
        with open(BOOK_LOG_PATH, "wb") as pickle_out:
            pickle.dump(all_books, pickle_out)
        
        return all_books