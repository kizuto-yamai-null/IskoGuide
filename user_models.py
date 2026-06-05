# user_models.py
from abc import ABC, abstractmethod

class User(ABC):
    """
    ⭐ OOP PILLAR 1: ABSTRACTION
    Enforces a strict architectural blueprint for all system users via an Abstract Base Class (ABC). 
    This class cannot be directly instantiated; it serves purely as a structural template.
    """
    def __init__(self, role_choice: int, email: str = "Public"):
        self.role_choice = role_choice  # 1: Admin, 2: Moderator, 3: Student, 4: Visitor
        self.email = email              # Track identity across authenticated states

    @abstractmethod
    def check_password(self, input_password: str) -> bool:
        """
        An abstract method forcing all subclasses to establish their own custom
        authentication validation processes.
        """
        pass


class Visitor(User):
    """
    ⭐ OOP PILLAR 2: POLYMORPHISM (Variant 1)
    Represents unauthenticated users (Guests) browsing public campus datasets. 
    They require no verification credentials and have no passwords, so their polymorphism rule 
    automatically bypasses credentials and returns False for security validations.
    """
    def __init__(self):
        # Calls the parent constructor to set up role attributes
        super().__init__(role_choice=4, email="Guest_User")

    def check_password(self, input_password: str) -> bool:
        return False  # Guests are strictly view-only and hold no credentials


class Student(User):
    """
    ⭐ OOP PILLAR 3: INHERITANCE
    Inherits fundamental core user attributes (role_choice, email) seamlessly from the User base class.
    
    ⭐ OOP PILLAR 4: ENCAPSULATION
    The student password variable is hidden as a private attribute using the double underscore 
    prefix (__password) to shield sensitive security data from outer system layers.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=3, email=email)
        self.__password = password  # Encapsulated private attribute
        self.my_posts = []

    def check_password(self, input_password: str) -> bool:
        """
        ⭐ OOP PILLAR 2: POLYMORPHISM (Variant 2)
        Implements a specific verification method to compare input against the encapsulated password.
        """
        return self.__password == input_password


class Moderator(User):
    """
    Inherits from User. Implements elevated forum queue permissions.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=2, email=email)
        self.__password = password  # Encapsulated private attribute

    def check_password(self, input_password: str) -> bool:
        """
        ⭐ OOP PILLAR 2: POLYMORPHISM (Variant 3)
        Implements specific verification method matches for Moderator scopes.
        """
        return self.__password == input_password


class Admin(User):
    """
    Inherits from User. Implements full system administration control access rights.
    """
    def __init__(self, email: str, password: str):
        super().__init__(role_choice=1, email=email)
        self.__password = password  # Encapsulated private attribute

    def check_password(self, input_password: str) -> bool:
        """
        ⭐ OOP PILLAR 2: POLYMORPHISM (Variant 4)
        Implements specific verification method matches for Admin scopes.
        """
        return self.__password == input_password
    