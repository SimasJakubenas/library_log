from utility.clear import clear


def add_book_view(line_position):
    if line_position.empty_line == True:
        print("")

    print("-" * 80)
    print(" " * 29 + "Add a book to library")
    print("-" * 80 + "\n")