# modules/scholarship.py

class ScholarshipModule:
    def __init__(self):
        """
        Initializes the Scholarship and Financial Assistance Engine.
        """
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Populate these strings with grant overviews, submission timelines, and contact info.
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
        """
        Lead Architect Algorithm: Evaluates academic and financial baselines 
        to compute a strict boolean gate eligibility status.
        """
        # 1. Setup threshold criteria rules (Using mock rules for TDP and Academic Grants)
        criteria_matrix = {
            "Tulong Dunong Program (TDP)": {
                "max_gwa": 2.50,        # Must be 2.50 or better (lower numerical value)
                "max_income": 30000.00  # Max family monthly income cap
            },
            "University Merit Scholarship": {
                "max_gwa": 1.75,        # Stricter academic standard
                "max_income": 50000.00  # Higher income cap allowed
            }
        }

        # Handle edge case where an invalid scholarship type is chosen
        if scholarship_type not in criteria_matrix:
            return {
                "is_eligible": False,
                "reason": "Unknown or unsupported scholarship program selection.",
                "status_code": 400
            }

        limits = criteria_matrix[scholarship_type]
        reasons_for_denial = []

        # 2. Perform the Mathematical Checks
        # Check Grade Weighted Average (Lower numbers mean better grades at PUP)
        if gwa > limits["max_gwa"]:
            reasons_for_denial.append(f"GWA of {gwa:.2f} exceeds the maximum limit of {limits['max_gwa']:.2f}.")

        # Check Household Income Cap
        if monthly_income > limits["max_income"]:
            reasons_for_denial.append(f"Monthly household income of ₱{monthly_income:,.2f} exceeds the ceiling of ₱{limits['max_income']:,.2f}.")

        # 3. Calculate Final Boolean States
        is_eligible = len(reasons_for_denial) == 0

        # 4. Generate custom diagnostic summary strings
        if is_eligible:
            status_message = f"Congratulations! You meet all baseline criteria for the {scholarship_type}."
        else:
            status_message = f"Ineligible for {scholarship_type}. Reasons: " + " | ".join(reasons_for_denial)

        return {
            "is_eligible": is_eligible,
            "status_message": status_message,
            "checked_gwa": gwa,
            "checked_income": monthly_income
        }