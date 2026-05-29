# user_models.py
from abc import ABC, abstractmethod

class User(ABC):
    """
    Demonstrates ABSTRACTION: This Abstract Base Class enforces the blueprint 
    for all system users. It cannot be instantiated directly.
    """
    def __init__(self, role_choice: int, email: str = "Public"):
        self.role_choice = role_choice  # 1: Admin, 2: Moderator, 3: Student, 4: Visitor
        self.email = email              # Track identity across authenticated states


class Visitor(User):
    """
    Represents unauthenticated users (Guests) browsing public campus datasets.
    They require no verification credentials and are limited to VIEW-ONLY access.
    """
    def __init__(self):
        super().__init__(role_choice=4, email="Guest_User")


class Student(User):
    """
    Demonstrates INHERITANCE: Inherits fundamental user attributes from User.
    Represents authenticated students who can submit posts once verified.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=3, email=email)
        # Demonstrates ENCAPSULATION: Passwords are treated as private attributes
        # using the double underscore prefix to secure data validation.
        self.__password = password  
        self.my_posts = []

    def check_password(self, input_password: str) -> bool:
        """
        Public method to check credentials safely without exposing the 
        private __password variable directly to outer system layers.
        """
        return self.__password == input_password


class Moderator(User):
    """
    Represents users with elevated content moderation and forum queue permissions.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=2, email=email)
        self.__password = password

    def check_password(self, input_password: str) -> bool:
        return self.__password == input_password


class Admin(User):
    """
    Represents system administrators with full platform control and configuration access.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=1, email=email)
        self.__password = password

    def check_password(self, input_password: str) -> bool:
        return self.__password == input_password