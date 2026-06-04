# modules/admission.py
from mock_data import admission_requirements_matrix

class AdmissionModule:
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 2: BUSINESS LOGIC LAYER
    This module enforces the evaluation algorithms, checklist compilation, 
    and document validation logic for all student categories. It acts as an 
    isolated logical component processing data inputs before committing state flags.
    """
    def __init__(self):
        # Load the newly refined requirement matrices from Layer 3 Storage
        self.requirements_pool = admission_requirements_matrix

    def show_Enrollment_Guide(self):
        """Returns a generic master collection list across all enrollment pipelines."""
        master_list = []
        for track, docs in self.requirements_pool.items():
            master_list.extend(docs)
        return list(set(master_list)) # Returns unique checklist entries safely

    def list_Requirements(self, gwa=1.0):
        """Returns baseline threshold informational arrays for registration."""
        return [f"General Weighted Average evaluation baseline: {gwa}. Verification tracking active."]

    def check_submission_eligibility(self, student_type, submitted_docs):
        """
        Dynamically filters checklists based on student_type. Checks incoming checkboxes 
        strictly against the tailored documents required for that track.
        """
        # Clean and safely map student type string input
        target_track = "Freshman"
        if student_type and "transferee" in student_type.lower():
            target_track = "Transferee"
        elif student_type and "returnee" in student_type.lower():
            target_track = "Returnee"

        required_docs = self.requirements_pool.get(target_track, self.requirements_pool["Freshman"])
        
        if not submitted_docs:
            return {"is_eligible": False, "missing": required_docs, "message": f"No files provided yet for the {target_track} stream."}
            
        # Filter logic tracking missing arrays
        missing_docs = [doc for doc in required_docs if doc not in submitted_docs]
        
        if len(missing_docs) == 0:
            return {
                "is_eligible": True,
                "message": f"Documentation complete! All parameters satisfied for a secure {target_track} entry path."
            }
        else:
            return {
                "is_eligible": False,
                "missing": missing_docs,
                "message": f"Action Required: You have {len(missing_docs)} missing requirements specific to your {target_track} status."
            }
        