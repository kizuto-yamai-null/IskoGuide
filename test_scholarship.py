import unittest
from modules.scholarship import ScholarshipModule

class TestScholarshipModule(unittest.TestCase):
    def setUp(self):
        self.scholarship = ScholarshipModule()

    # 1. Test Success: Pasok sa criteria
    def test_eligible_student(self):
        result = self.scholarship.evaluate_eligibility(1.50, 20000.00, "Tulong Dunong Program (TDP)")
        self.assertTrue(result["is_eligible"])
        self.assertIn("Congratulations", result["status_message"])

    # 2. Test Failure: Lampas sa GWA
    def test_ineligible_gwa(self):
        # GWA na 2.60 ay lampas sa 2.50 threshold ng TDP
        result = self.scholarship.evaluate_eligibility(2.60, 20000.00, "Tulong Dunong Program (TDP)")
        self.assertFalse(result["is_eligible"])
        self.assertIn("higher than the required", result["status_message"])

    # 3. Test Failure: Lampas sa Income
    def test_ineligible_income(self):
        # Income na 60k ay lampas sa 50k threshold ng Merit Scholarship
        result = self.scholarship.evaluate_eligibility(1.50, 60000.00, "University Merit Scholarship")
        self.assertFalse(result["is_eligible"])
        self.assertIn("exceeds the", result["status_message"])

    # 4. Test Edge Case: Unsupported scholarship type
    def test_unknown_scholarship(self):
        result = self.scholarship.evaluate_eligibility(1.0, 1000, "Fake Scholarship")
        self.assertFalse(result["is_eligible"])
        self.assertEqual(result["status_message"], "Unknown or unsupported scholarship program selection.")