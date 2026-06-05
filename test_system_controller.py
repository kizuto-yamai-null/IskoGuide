import unittest
from unittest.mock import patch
from system_controller import IskoGuideController 
import os

class TestSystemController(unittest.TestCase):
    def setUp(self):
        # I-clear ang accounts.csv bago ang bawat test para hindi magka-conflict sa data
        if os.path.exists("accounts.csv"):
            os.remove("accounts.csv")
            
        with patch('modules.admission.AdmissionModule'), \
             patch('modules.scholarship.ScholarshipModule'), \
             patch('modules.directory.CampusDirectory'), \
             patch('modules.forum.ForumModule'), \
             patch('modules.about.AboutModule'):
            self.controller = IskoGuideController()
    
    def test_register_student_success(self):
        email = "test@edu.ph"
        password = "pass123"
        success, message = self.controller.register_student(email, password)
        
        # Dito natin ilalagay ang diagnostic message para malaman natin kung bakit nag-False
        self.assertTrue(success, msg=f"Registration failed! Message received: {message}")
        self.assertEqual(len(self.controller.registered_students), 1)

    # ... (yung ibang tests mo ay mananatili nang ganyan)

    def tearDown(self):
        # Linisin ulit pagkatapos ng tests
        if os.path.exists("accounts.csv"):
            os.remove("accounts.csv")

if __name__ == '__main__':
     unittest.main()