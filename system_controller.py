# system_controller.py
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

# Import the Student model class to instantiate student records
from user_models import Student

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
        self.__secret_pin = 0        # Admin authentication threshold
        self.__moderator_pin = 1111  # Moderator authentication threshold
        
        # System Mock Database Storage for Registered Student Objects
        self.registered_students = []

    def verify_credentials(self, role: int, PIN_attempt: int) -> bool:
        """
        Processes staff credential security matches (Admin/Mod PIN validation).
        """
        if role == 1:    # Admin validation
            return PIN_attempt == self.__secret_pin
        elif role == 2:  # Moderator validation
            return PIN_attempt == self.__moderator_pin
        return False     # Visitor/Student handles verification differently

    def register_student(self, email: str, password: str) -> tuple[bool, str]:
        """
        Validates student credentials, checks for duplication records, 
        and stores a new Student object into the system. Fully guarded against TypeErrors.
        """
        # 🛡️ TYPE GUARD: Defensive cast to string if an integer or invalid type bypasses the form
        if not isinstance(email, str):
            email = str(email)
        if not isinstance(password, str):
            password = str(password)

        # Basic validation rules
        if "@" not in email or "." not in email:
            return False, "Invalid email format! Please use a valid email."
            
        # Check if the student email already exists in our collection
        for student in self.registered_students:
            if student.email == email:
                return False, "This email is already registered!"
                
        # OOP Instantiation: Create the Student object and save it
        new_student = Student(email, password)
        self.registered_students.append(new_student)
        return True, "Registration successful!"

    def verify_student(self, email: str, password: str) -> bool:
        """
        Searches the student collection and uses encapsulated verification 
        methods to validate incoming passwords. Fully guarded against TypeErrors.
        """
        # 🛡️ TYPE GUARD: Ensure inputs are treated strictly as string variables
        if not isinstance(email, str) or not isinstance(password, str):
            email = str(email)
            password = str(password)

        for student in self.registered_students:
            if student.email == email:
                # Utilizes the encapsulated check_password method from the Student object
                return student.check_password(password)
        return False
    