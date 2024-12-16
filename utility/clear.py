import os


def clear():
    """
    Clears the terminal screen using os.system() function
    """
    os.system('cls' if os.name == 'nt' else 'clear')