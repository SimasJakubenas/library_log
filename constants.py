import math


BOOK_LOG_PATH = r"D:\codeacademy_darbai\library_log\pickle_files\book_log.pkl"
USER_LOG_PATH = r"D:\codeacademy_darbai\library_log\pickle_files\user_log.pkl"

PAGINATION = 5

BOOK_GENRES = [
    "Fantasy",
    "Scy-Fy",
    "Mystery",
    "Thriller",
    "Romance",
    "Hist Fiction",
    "Horror",
    "Non-Fiction",
    "Biography",
    "Self-Help",
    "Graphic Novel",
    "Young Adult",
    "Children's",
    "Adventure",
    "Dystopian",
    "Poetry",
    "Classic",
    "Crime",
    "Memoir",
    "Humor"
]

# Counts a number of rows for the book genre display based on 4 columns
BOOK_GENRES_SPLIT = math.ceil(len(BOOK_GENRES) / 4)

BORROWING_TIME = 20