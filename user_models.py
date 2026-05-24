# user_models.py
from abc import ABC, abstractmethod

class User(ABC):
    """
    Abstract Base Class for defining common user properties and enforcing role interfaces.
    """
    def __init__(self, role_choice: int):
        self.role_choice = role_choice  # 1: Admin, 2: Moderator, 3: Visitor

class Visitor(User):
    """
    Represents unauthenticated users browsing public campus datasets.
    """
    def __init__(self):
        super().__init__(role_choice=3)

class Moderator(User):
    """
    Represents users with elevated content moderation permissions.
    """
    def __init__(self):
        super().__init__(role_choice=2)

class Admin(User):
    """
    Represents system administrators with full database and state alteration access.
    """
    def __init__(self):
        super().__init__(role_choice=1)