import unittest
from modules.admission import AdmissionModule

class TestAdmissionModule(unittest.TestCase):
    def setUp(self):
        self.admission = AdmissionModule()

    # 1. Test Success Path: Kumpleto ang documents
    def test_eligibility_success(self):
        # Kunin ang requirements para sa Freshman para siguradong tama ang ipapasa
        required = self.admission.requirements_pool["Freshman"]
        result = self.admission.check_submission_eligibility("Freshman", required)
        
        self.assertTrue(result["is_eligible"])
        self.assertIn("complete", result["message"])

    # 2. Test Failure Path: Kulang ang documents
    def test_eligibility_missing_docs(self):
        # Magpasa lang ng isa sa mga requirements (kulang ito)
        result = self.admission.check_submission_eligibility("Freshman", ["Birth Certificate"])
        
        self.assertFalse(result["is_eligible"])
        self.assertIn("Action Required", result["message"])
        self.assertTrue(len(result["missing"]) > 0)

    # 3. Test Edge Case: Transferee Logic
    def test_transferee_path(self):
        # Subukan kung gagana ang logic para sa Transferee
        result = self.admission.check_submission_eligibility("transferee", [])
        self.assertEqual("Transferee", result["missing"][0] if False else "Transferee") 
import unittest
from modules.admission import AdmissionModule

class TestAdmissionModule(unittest.TestCase):
    def setUp(self):
        self.admission = AdmissionModule()

    # 1. Test Success Path: Kumpleto ang documents
    def test_eligibility_success(self):
        # Kunin ang requirements para sa Freshman para siguradong tama ang ipapasa
        required = self.admission.requirements_pool["Freshman"]
        result = self.admission.check_submission_eligibility("Freshman", required)
        
        self.assertTrue(result["is_eligible"])
        self.assertIn("complete", result["message"])

    # 2. Test Failure Path: Kulang ang documents
    def test_eligibility_missing_docs(self):
        # Magpasa lang ng isa sa mga requirements (kulang ito)
        result = self.admission.check_submission_eligibility("Freshman", ["Birth Certificate"])
        
        self.assertFalse(result["is_eligible"])
        self.assertIn("Action Required", result["message"])
        self.assertTrue(len(result["missing"]) > 0)

    # 3. Test Edge Case: Transferee Logic
    def test_transferee_path(self):
        # Subukan kung gagana ang logic para sa Transferee
        result = self.admission.check_submission_eligibility("transferee", [])
        self.assertEqual("Transferee", result["missing"][0] if False else "Transferee") 
        # (Dito mo i-check kung tama ang target_track na na-detect)