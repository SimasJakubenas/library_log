class Library:
    def __init__(self):
        self.book_list = []
    
    def add_book(self, book):
        self.book_list.append(book)
        print(f"{book.title} added to library")
    
    def remove_book(self, title):
        for book in self.book_list:
            if book.title == title:
                self.book_list.remove(book)
                print(f"{title} removed from library")
                
        print(f"{title} not found in library")