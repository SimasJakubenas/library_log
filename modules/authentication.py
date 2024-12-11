from classes.library import Library


def register():
    library_initiation = Library()
    while True:
        username = input("Enter your username: ")
        
        if not username.isalnum():
            print("Username can only contain alphanumeric characters.")
            continue
        
        if len(username) < 6:
            print("Username must be at least 6 characters long.")
            continue
        
        elif len(username) > 20:
            print("Username must be no more than 20 characters long.")
            continue
        
        for user_instance in library_initiation:
            if user_instance.username == username:
                print("Username already exists. Please choose a different one.")
                continue

        break
        
    while True:
        password = input("Enter your password: ")
        
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        
        elif len(password) > 20:
            print("Password must be no more than 20 characters long.")
            continue
        
        for char in password:
            if not any(char.isdigit()):
                print("Password must contain at least one digit.")
                continue
                
            if not any(char.isalpha()):
                print("Password must contain at least one letter.")
                continue
                
            if not any(char.isupper()):
                print("Password must contain at least one uppercase letter.")
                continue
                
            if not any(char.islower()):
                print("Password must contain at least one lowercase letter.")
                continue
        
        break
    
    while True:
        confirm_password = input("Confirm your password: ")
        
        if password!= confirm_password:
            print("Passwords do not match.")
            continue
            
        break
    
    for user_instance in library_initiation:
        print(user_instance.username)
register()