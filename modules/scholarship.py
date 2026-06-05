# modules/scholarship.py

# 🏢 FIXED: Pull the newly seeded data arrays from the mock database
from mock_data import scholarship_guidelines_text, scholarship_deadlines_matrix

class ScholarshipModule:
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 2: BUSINESS LOGIC LAYER
    This module encapsulates the mathematical evaluation engines, threshold validations, 
    and policy constraints for institutional and national grants. It ingests primitive numerical
    inputs from Layer 1 forms and performs strict matrix operations against Layer 3 criteria sets.
    """
    def __init__(self):
        """
        Initializes the Scholarship and Financial Assistance Engine.
        """
        # ==============================================================================
        # 📝 DATA SEEDING & STATIC TEXT DATA POOL
        # 🏢 3-LAYER ARCHITECTURE - LAYER 3 CONNECTIVITY
        # Properties now pull from the centralized mock data file
        # ==============================================================================
        self.grant_guidelines = scholarship_guidelines_text
        self.application_deadlines = scholarship_deadlines_matrix

    def get_grant_guidelines(self) -> str:
        return self.grant_guidelines

    def get_deadlines(self) -> dict:
        return self.application_deadlines

    # ==============================================================================
    # 🧠 EVALUATION ENGINE
    # ==============================================================================
    def evaluate_eligibility(self, gwa: float, monthly_income: float, scholarship_type: str) -> dict:
        """Evaluates mathematical GWA limits and family income boundaries."""
        # Added the DOST-SEI parameter threshold matrix limits
        criteria_matrix = {
            "Tulong Dunong Program (TDP)": {
                "max_gwa": 2.50,        
                "max_income": 33333.00  # ~Php 400,000 annual gross ceiling
            },
            "University Merit Scholarship": {
                "max_gwa": 1.75,        
                "max_income": 50000.00  
            },
            "DOST-SEI Undergraduate Scholarship": {
                "max_gwa": 1.75,        # 85% grade average equivalent
                "max_income": 41666.00  # Php 500,000 annual gross ceiling
            }
        }

        if scholarship_type not in criteria_matrix:
            return {
                "is_eligible": False,
                "status_message": "Unknown or unsupported scholarship program selection."
            }

        limits = criteria_matrix[scholarship_type]
        reasons_for_denial = []

        if gwa > limits["max_gwa"]:
            reasons_for_denial.append(f"GWA of {gwa:.2f} is higher than the required {limits['max_gwa']:.2f} threshold.")

        if monthly_income > limits["max_income"]:
            reasons_for_denial.append(f"Monthly household income of ₱{monthly_income:,.2f} exceeds the ₱{limits['max_income']:,.2f} ceiling.")

        is_eligible = len(reasons_for_denial) == 0

        if is_eligible:
            status_message = f"Congratulations! You meet all baseline criteria for the {scholarship_type}."
        else:
            status_message = f"Ineligible for {scholarship_type}. Reason(s): " + " | ".join(reasons_for_denial)

        return {
            "is_eligible": is_eligible,
            "status_message": status_message,
            "checked_gwa": gwa,
            "checked_income": monthly_income
        }
    