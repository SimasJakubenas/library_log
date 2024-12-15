import pickle
import os
from constants import *
from classes.library_user import Library_user
from classes.book import Book


class Library:
    def __init__(self, user_list = []):
        self.user_list = user_list
    
    def add_book(self, book):

        if os.path.isfile(BOOK_LOG_PATH) and os.stat(BOOK_LOG_PATH).st_size != 0:
            with open(BOOK_LOG_PATH, "rb") as pickle_in:
                old_list:list = pickle.load(pickle_in)
                
                updated_list = old_list + [book]
                
            with open(BOOK_LOG_PATH, "wb") as pickle_out:
                pickle.dump(updated_list, pickle_out)
                
        else:
            with open(BOOK_LOG_PATH, "wb") as pickle_out:
                pickle.dump([book], pickle_out)
    
    # def remove_book(self, title):
        # for book in self.book_list:
        #     if book.title == title:
        #         self.book_list.remove(book)
        #         print(f"{title} removed from library")
                
        # print(f"{title} not found in library")
    
    def add_user(self, username, password, line_position):

        new_user = Library_user(username, password)
        
        if os.path.isfile(USER_LOG_PATH) and os.stat(USER_LOG_PATH).st_size != 0:
            with open(USER_LOG_PATH, "rb") as pickle_in:
                old_list:list = pickle.load(pickle_in)
                
            for user in old_list:
                if user.username == username:
                    line_position.empty_line = False
                    print("Username already exists")
                    return None
            
            updated_list = [new_user] + old_list
            with open(USER_LOG_PATH, "wb") as pickle_out:
                pickle.dump(updated_list, pickle_out)
                line_position.empty_line = False
                print(f"{username} added to user list")
                
        else:
            with open(USER_LOG_PATH, "wb") as pickle_out:
                pickle.dump([new_user], pickle_out)
                line_position.empty_line = False
                print(f"{username} added to user list")
        
        return new_user
    
    def authenticate_user(self, username, password, line_position):
        
        with open(USER_LOG_PATH, "rb") as pickle_in:
            user_list:list = pickle.load(pickle_in)
            
        for user in user_list:
            if user.username == username and user.password == password:
                print("Authentication successful")
                line_position.empty_line = False
                return user
        
        print("Authentication failed")
        