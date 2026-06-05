# test_auth.py
import os
import unittest
from unittest.mock import patch
from website import create_app

class TestAuth(unittest.TestCase):
    def setUp(self):
        # Initialize the app with testing configuration
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for easier testing
        
        # Fallback directory setup to keep configurations safe
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.app.template_folder = os.path.join(base_dir, 'website', 'templates')
        
        self.client = self.app.test_client()

    # --- HAPPY PATH TESTS ---
    def test_signup_and_student_login_success(self):
        # 1. Register a student
        self.client.post('/signup', data={'email': 'happy@student.edu.ph', 'password': 'Password123'})
        
        # 2. Login as that student
        response = self.client.post('/login', data={
            'role_choice': '3',
            'email': 'happy@student.edu.ph',
            'password': 'Password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)

    def test_admin_login_success(self):
        # Admin login with correct default PIN 0
        response = self.client.post('/login', data={
            'role_choice': '1',
            'pin_input': '0'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)

    # --- ERROR PATH TESTS ---
    # 🎯 FIX: Patch render_template specifically for this invalid PIN response route
    @patch('website.auth.render_template')
    def test_login_invalid_pin(self, mock_render):
        # Configure the mock to return a clean string payload instead of parsing disk files
        mock_render.return_value = "Invalid Security PIN. Access Denied."
        
        # Attempt Admin login with wrong PIN
        response = self.client.post('/login', data={
            'role_choice': '1',
            'pin_input': '9999'
        })
        
        # Verify that our backend logic successfully caught the bad PIN and attempted to render the error
        mock_render.assert_called_with("login.html", error="Invalid Security PIN. Access Denied.")

    def test_signup_invalid_email(self):
        # Attempt signup with malformed email
        response = self.client.post('/signup', data={
            'email': 'bademail',
            'password': 'password'
        })
        self.assertIn(b"Invalid email format", response.data)

if __name__ == '__main__':
    unittest.main()
    
