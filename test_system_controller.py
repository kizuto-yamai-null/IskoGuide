import unittest
from unittest.mock import patch
# Import directly since it is in the same folder
from system_controller import IskoGuideController 

class TestSystemController(unittest.TestCase):
    def setUp(self):
        # Patch modules based on where they are defined in system_controller
        with patch('modules.admission.AdmissionModule'), \
             patch('modules.scholarship.ScholarshipModule'), \
             patch('modules.directory.CampusDirectory'), \
             patch('modules.forum.ForumModule'), \
             patch('modules.about.AboutModule'):
            
            self.controller = IskoGuideController()
    
    def test_register_student_success(self):
        success, message = self.controller.register_student("test@edu.ph", "pass123")
        self.assertTrue(success)
        self.assertEqual(len(self.controller.registered_students), 1)

    def test_register_student_duplicate(self):
        self.controller.register_student("test@edu.ph", "pass123")
        success, message = self.controller.register_student("test@edu.ph", "pass123")
        self.assertFalse(success)
        self.assertEqual(message, "This email is already registered!")

    def test_register_student_invalid_email(self):
        # Test case: Missing @ and .
        success, message = self.controller.register_student("invalidemail.com", "pass123")
        self.assertFalse(success)
        self.assertEqual(message, "Invalid email format! Please use a valid email.")

    def test_verify_student_logic(self):
        self.controller.register_student("test@edu.ph", "pass123")
        # Valid verification
        self.assertTrue(self.controller.verify_student("test@edu.ph", "pass123"))
        # Invalid password
        self.assertFalse(self.controller.verify_student("test@edu.ph", "wrong"))

    def test_verify_credentials(self):
        # Admin role is 1, default PIN is 0
        self.assertTrue(self.controller.verify_credentials(1, 0))
        # Moderator role is 2, default PIN is 1111
        self.assertTrue(self.controller.verify_credentials(2, 1111))
        # Invalid role/PIN
        self.assertFalse(self.controller.verify_credentials(3, 1234))

if __name__ == '__main__':
     unittest.main()
