from classes.user import User


class Library:
    def __init__(self, user_list = []):
        self.book_list = []
        self.user_list = user_list
    
    def add_book(self, book):
        self.book_list.append(book)
        print(f"{book.title} added to library")
    
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