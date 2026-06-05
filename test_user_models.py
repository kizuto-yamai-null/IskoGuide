import unittest
from user_models import Student, Visitor, Admin, Moderator

class TestUserModels(unittest.TestCase):
    
    # --- STUDENT TESTS ---
    def test_student_initialization(self):
        student = Student("student@iskoguide.edu.ph", "password123")
        self.assertEqual(student.email, "student@iskoguide.edu.ph")
        self.assertEqual(student.role_choice, 3)
        self.assertEqual(len(student.my_posts), 0)

    def test_student_password_validation(self):
        student = Student("student@iskoguide.edu.ph", "secure123")
        self.assertTrue(student.check_password("secure123"))
        self.assertFalse(student.check_password("wrongpass"))

    def test_student_encapsulation(self):
        student = Student("test@test.com", "pass")
        # Verify private attribute is not directly accessible
        with self.assertRaises(AttributeError):
            print(student.__password)

    # --- VISITOR TESTS ---
    def test_visitor_setup(self):
        visitor = Visitor()
        self.assertEqual(visitor.role_choice, 4)
        self.assertEqual(visitor.email, "Guest_User")

    # --- ADMIN/MODERATOR TESTS ---
    def test_admin_check_password(self):
        admin = Admin("admin@iskoguide.edu.ph", "adminpin")
        self.assertTrue(admin.check_password("adminpin"))
        self.assertFalse(admin.check_password("12345"))

    def test_moderator_check_password(self):
        mod = Moderator("mod@iskoguide.edu.ph", "modpin")
        self.assertTrue(mod.check_password("modpin"))

    # --- INVALID DATA HANDLING ---
    def test_invalid_data_graceful_handling(self):
        """Ensure system doesn't crash with empty/unexpected input types."""
        student = Student("", "")
        self.assertFalse(student.check_password("anything"))
        
        # Test type-sensitivity
        admin = Admin("admin@edu.ph", "123")
        self.assertFalse(admin.check_password(123)) # Integer vs String

if __name__ == '__main__':
     unittest.main()
