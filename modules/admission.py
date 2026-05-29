# modules/admission.py

class AdmissionModule:
    def __init__(self):
        """
        Initializes the admission engine.
        """
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Populate these properties with official text guidelines and step sequences.
        # ==============================================================================
        self.enrollment_steps = ""
        self.requirements = []

    def show_Enrollment_Guide(self) -> str: 
        return self.enrollment_steps

    def list_Requirements(self, gwa: float) -> list: 
        return self.requirements

    def Get_Admission_FAQ(self): 
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Return a dictionary or list of frequently asked questions regarding PUP admissions.
        # ==============================================================================
        pass

    # ==============================================================================
    # 🧠 LEAD ARCHITECT LOGIC (66%): EVALUATION ENGINE
    # ==============================================================================
    def check_submission_eligibility(self, student_type: str, submitted_documents: list) -> dict:
        """
        Evaluates submitted documents against the track benchmarks.
        """
        requirements_map = {
            "Freshman": ["Grade 12 Report Card", "PUPCET Results", "Birth Certificate"],
            "Transferee": ["Official Transcript of Records (TOR)", "Honorable Dismissal"],
            "Irregular": ["Informative Copy of Grades", "Approved Readmission Form"]
        }
        
        mandatory_checklist = requirements_map.get(student_type, [])
        missing_documents = [doc for doc in mandatory_checklist if doc not in submitted_documents]
        is_eligible = len(missing_documents) == 0
        
        if is_eligible:
            status_message = f"Clear for Enrollment! All mandatory {student_type} items verified."
        else:
            status_message = f"Action Required: Missing mandatory prerequisite documents."
            
        return {
            "is_eligible": is_eligible,
            "missing_documents": missing_documents,
            "status_message": status_message
        }