from classes.user import User


class Admin(User):
    def __init__(self,username, password):
        super().__init__(username, password)
        self.is_admin = True