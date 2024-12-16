import datetime

class Book:
    def __init__(self, title, author, publication_year, genre, quantity, is_overdue=False, borrow_time=None):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.quantity = quantity
        self.is_overdue = is_overdue
        self.borrow_time = borrow_time
        
    def __str__(self):
        return f"{self.title:<30}| {self.author:<18}| {self.publication_year:<4}| {self.genre:13}|"
    
    def borrowing_time(self):
        data = datetime.datetime.now()
        seconds = (data - datetime.datetime(1970,1,1)).total_seconds()
        self.borrow_time = seconds
    
    def reset_borrowing_time(self):
        self.borrow_time = None