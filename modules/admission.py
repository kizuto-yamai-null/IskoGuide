# modules/admission.py
from mock_data import admission_steps

class AdmissionModule:
    def __init__(self):
        self.steps_pool = admission_steps

    def show_Enrollment_Guide(self):
        """Upgraded from print: Returns the clean steps array to render on web views."""
        return self.steps_pool

    def list_Requirements(self, gwa=1.0):
        """Baseline structural helper required by system controller specs."""
        return [f"Maintain standard compliance thresholds (Current baseline filter: {gwa})"]

    def check_submission_eligibility(self, student_type, submitted_docs):
        """
        Processes form checkboxes from the frontend to determine if the 
        student has supplied all documents from Enrico's checklist array.
        """
        if not submitted_docs:
            return {"is_eligible": False, "missing": self.steps_pool, "message": "No documents submitted yet."}
            
        missing_docs = [step for step in self.steps_pool if step not in submitted_docs]
        
        if len(missing_docs) == 0:
            return {
                "is_eligible": True,
                "message": f"Congratulations! Your documentation is complete for a {student_type} submission track."
            }
        else:
            return {
                "is_eligible": False,
                "missing": missing_docs,
                "message": f"Pending Action: You have {len(missing_docs)} missing document requirements left to supply."
            }