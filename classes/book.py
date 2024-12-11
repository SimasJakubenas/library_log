class Book:
    def __init__(self, title, author, publication_year, genre, quantity, is_overdue=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.quantity = quantity
        is_overdue = is_overdue
        