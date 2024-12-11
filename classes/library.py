import pickle
import os
from constants import *
from classes.user import User
from classes.book import Book


class Library:
    def __init__(self, user_list = []):
        self.book_list = []
        self.user_list = user_list
    
    def add_book(self, book):
        self.book_list.append(book)

        if os.path.isfile(BOOK_LOG_PATH) and os.stat(BOOK_LOG_PATH).st_size != 0:
            with open(BOOK_LOG_PATH, "rb") as pickle_in:
                old_list:list = pickle.load(pickle_in)
                
                updated_list = self.book_list + old_list
                
            with open(BOOK_LOG_PATH, "wb") as pickle_out:
                pickle.dump(updated_list, pickle_out)
                
                for x in updated_list:
                    print(x.title)
                
        else:
            with open("pickle_files/book_log.pkl", "wb") as pickle_out:
                pickle.dump([book], pickle_out)
    
    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)
                print(f"{title} removed from library")
                
        print(f"{title} not found in library")
    
    def add_user(self, username, password):
        for user in self.user_list:
            if user.username == username:
                print("Username already exists")
                return
        
        new_user = User(username, password)
        self.user_list.append(new_user)
        print(f"{username} added to user list")
        
        return new_user
    
    def authenticate_user(self, username, password):
        for user in self.user_list:
            
            if user.username == username and user.password == password:
                print("Authentication successful")
                return user
        
        print("Authentication failed")