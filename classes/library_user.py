from classes.user import User


class Library_user(User):
    def __init__(self, name, username, password, have_overdue=False):
        super().__init__(name, username, password)
        self.have_overdue = have_overdue
        self.borrowed_books = []
        
        def borrow_books(self, book):
            if len(self.borrowed_books) < 5:
                self.borrowed_books.append(book)
                print(f"{book.title} has been borrowed")
                
            else:
                print("You have reached your borrowing limit")
        
        def return_book(self, book):
            self.my_books.remove(book)
            print(f"{book.title} has been returned")
        
        def show_my_books(self):
            if self.my_books:
                print("My current books:")
                for book in self.my_books:
                    print(f"{book.title}")
            else:
                print("You haven't borrowed any books yet")