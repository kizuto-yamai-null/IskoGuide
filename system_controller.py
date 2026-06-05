# system_controller.py
import os
import csv
from datetime import datetime

# Submodule Imports
from modules.admission import AdmissionModule
from modules.scholarship import ScholarshipModule
from modules.directory import CampusDirectory
from modules.forum import ForumModule
from modules.about import AboutModule

# Import the Student model class to instantiate student records
from user_models import Student

class IskoGuideController:
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 2: BUSINESS LOGIC LAYER
    This central controller coordinates system rules, data stream conversions,
    and security gates. It isolates the user-facing presentation routes (Layer 1)
    from direct structural file storage (Layer 3).
    """
    def __init__(self):
        # ⭐ OOP CONCEPT: COMPOSITION (HAS-A Relationship)
        # The IskoGuideController 'has' and owns these functional submodules.
        # They are instantiated together and their lifetimes are bound to the controller.
        self.admission_module = AdmissionModule()
        self.scholarship_module = ScholarshipModule()
        self.campus_directory = CampusDirectory()
        self.forum_module = ForumModule()
        self.about_module = AboutModule()
        
        # ⭐ OOP PILLAR: ENCAPSULATION (Private Variables)
        # Hidden behind a double underscore prefix to strictly prevent external system files 
        # from reading, overriding, or tampering with credential matching thresholds.
        self.__secret_pin = 0        # Admin authentication threshold
        self.__moderator_pin = 1111  # Moderator authentication threshold
        
        # 🏢 3-LAYER ARCHITECTURE - LAYER 3: DATA STORAGE LAYER (File Definitions)
        self.accounts_file = "accounts.csv"
        self.history_file = "login_history.csv"
        
        # System Runtime Database Storage Container
        # Maps {email: StudentObject} as key-value pairs for optimized O(1) performance lookups.
        self.registered_students = {}

        # Automatically execute file initialization guards and database boots on initialization
        self._initialize_csv_files()
        self._load_accounts_from_csv()

    def _initialize_csv_files(self):
        """Creates the database CSV files with headers in the ISKOGUIDE directory if they don't exist yet."""
        # 1. Initialize Accounts File Guard
        if not os.path.exists(self.accounts_file):
            with open(self.accounts_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["email", "password"]) # Permanent Storage Schema
                
        # 2. Initialize Security Audit Log File Guard
        if not os.path.exists(self.history_file):
            with open(self.history_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "email", "role", "status"]) # System Audit Trail Schema

    def _load_accounts_from_csv(self):
        """Reads permanent records from accounts.csv into system memory on runtime startup."""
        try:
            with open(self.accounts_file, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    email = row["email"]
                    password = row["password"]
                    if email:
                        # Re-instantiating the text row data back into a rich Student domain object
                        self.registered_students[email] = Student(email, password)
        except Exception as e:
            print(f"Database Initialization Read Error: {e}")

    def log_login_event(self, email: str, role: str, status: str):
        """Appends a timestamped security ledger log to login_history.csv."""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.history_file, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, email, role, status])
        except Exception as e:
            print(f"Failed to record security audit trail ledger: {e}")

    def verify_credentials(self, role: int, PIN_attempt: int) -> bool:
        """
        Processes staff credential security matches (Admin/Mod PIN validation) and logs results.
        """
        is_valid = False
        role_name = "Unknown Staff"
        
        # Validates attempts safely against private encapsulated parameters
        if role == 1:    # Admin validation
            role_name = "Admin"
            is_valid = (PIN_attempt == self.__secret_pin)
        elif role == 2:  # Moderator validation
            role_name = "Moderator"
            is_valid = (PIN_attempt == self.__moderator_pin)
            
        # Security Auditing System Trigger
        log_status = "Successful Login" if is_valid else "Failed Login (Invalid PIN)"
        log_identity = role_name if is_valid else f"Attempted_{role_name}"
        self.log_login_event(log_identity, role_name, log_status)
        
        return is_valid

    def register_student(self, email: str, password: str) -> tuple[bool, str]:
        """
        Validates student credentials, checks for duplication records, 
        and stores a new Student object into the system permanently. Fully guarded against TypeErrors.
        """
        # 🛡️ TYPE GUARD: Defensive cast to string if an integer or invalid type bypasses the form
        if not isinstance(email, str):
            email = str(email)
        if not isinstance(password, str):
            password = str(password)

        # Basic validation rules
        if "@" not in email or "." not in email:
            return False, "Invalid email format! Please use a valid email."
            
        # Check if the student email already exists in our dictionary storage collection
        if email in self.registered_students:
            return False, "This email is already registered!"
                
        try:
            # 1. Instantiate the object and map it directly to runtime dictionary memory
            new_student = Student(email, password)
            self.registered_students[email] = new_student
            
            # 2. Database Persistence: Append structural text parameters directly to flat files
            with open(self.accounts_file, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([email, password])
                
            return True, "Registration successful!"
        except Exception as e:
            return False, f"System storage engine failed: {str(e)}"

    def verify_student(self, email: str, password: str) -> bool:
        """
        Searches the student collection and uses encapsulated verification 
        methods to validate incoming passwords. Fully guarded against TypeErrors.
        """
        # 🛡️ TYPE GUARD: Ensure inputs are treated strictly as string variables
        if not isinstance(email, str) or not isinstance(password, str):
            email = str(email)
            password = str(password)

        is_valid = False
        status_msg = "Failed Login"
        
        # Direct lookup execution path
        if email in self.registered_students:
            # Utilizes the polymorphic, encapsulated verification method from user_models
            if self.registered_students[email].check_password(password):
                is_valid = True
                status_msg = "Successful Login"
                
        # Audit Trail Recording Trigger
        self.log_login_event(email, "Student", status_msg)
        return is_valid
    