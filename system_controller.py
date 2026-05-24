# system_controller.py
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

class IskoGuideController:
    """
    Core business logic controller that maintains instance management 
    of system submodules and coordinates state verification.
    """
    def __init__(self):
        # Composition: Instantiating and owning the functional submodules
        self.admission_module = AdmissionModule()
        self.scholarship_module = ScholarshipModule()
        self.campus_directory = CampusDirectory()
        self.forum_module = ForumModule()
        self.about_module = AboutModule()
        
        # Internal security parameters (Private variables encapsulated for safety)
        self.__secret_pin = 0      # Admin authentication threshold
        self.__moderator_pin = 1111  # Moderator authentication threshold

    def verify_credentials(self, role: int, PIN_attempt: int) -> bool:
        """
        Processes credential security matches. Returns True if authentication 
        succeeds, otherwise returns False.
        """
        if role == 1:    # Admin validation
            return PIN_attempt == self.__secret_pin
        elif role == 2:  # Moderator validation
            return PIN_attempt == self.__moderator_pin
        return False     # Visitor requires no PIN verification