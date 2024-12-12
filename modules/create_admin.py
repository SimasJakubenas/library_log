import os
import pickle
from dotenv import load_dotenv
from classes.admin import Admin
from utility.clear import clear
from constants import *


def create_admin():
    # Load variables from .env file
    load_dotenv()
    admin_user = Admin(os.getenv("ADMIN"), os.getenv("ADMIN_PASSWORD"))
    # Access and print value
    if os.path.isfile(USER_LOG_PATH) and os.stat(USER_LOG_PATH).st_size != 0:
        with open(USER_LOG_PATH, "rb") as pickle_in:
            old_list:list = pickle.load(pickle_in)
        
        username_list = []
        for user in old_list:
            username_list.append(user.username)
        
        updated_list = old_list
        
        if os.getenv("ADMIN") not in username_list:
            updated_list += [admin_user]
            
        with open(USER_LOG_PATH, "wb") as pickle_out:
            pickle.dump(updated_list, pickle_out)
            
    else:
        with open(USER_LOG_PATH, "wb") as pickle_out:
            pickle.dump([admin_user], pickle_out)
                
    admin_user = Admin(os.getenv("ADMIN"), os.getenv("ADMIN_PASSWORD"))
    clear()