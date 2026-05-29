# modules/scholarship.py

class ScholarshipModule:
    def __init__(self):
        """
        Initializes the Scholarship and Financial Assistance Engine.
        """
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Assign strings/dictionaries imported from mock_data.py here.
        # ==============================================================================
        self.grant_guidelines = ""
        self.application_deadlines = {}

    def get_grant_guidelines(self) -> str:
        return self.grant_guidelines

    def get_deadlines(self) -> dict:
        return self.application_deadlines

    # ==============================================================================
    # 🧠 LEAD ARCHITECT LOGIC (66%): EVALUATION ENGINE
    # ==============================================================================
    def evaluate_eligibility(self, gwa: float, monthly_income: float, scholarship_type: str) -> dict:
        """Evaluates mathematical GWA limits and family income boundaries."""
        criteria_matrix = {
            "Tulong Dunong Program (TDP)": {
                "max_gwa": 2.50,        
                "max_income": 30000.00  
            },
            "University Merit Scholarship": {
                "max_gwa": 1.75,        
                "max_income": 50000.00  
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