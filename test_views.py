import unittest
from website import create_app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    # 1. Test Public Pages
    def test_home_and_about_pages(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/aboutPUP').status_code, 200)

    # 2. Test Scholarship Input (Robustness Check)
    def test_scholarship_invalid_input(self):
        # 1. Just test that we get a 200 OK first, ignore content for a second
        response = self.client.post('/scholarship', 
                                    data={'gwa': 'not-a-number', 'income': '10000', 'scholarship_type': 'Academic'},
                                    content_type='application/x-www-form-urlencoded')
        
        # Print the status code - if it's 302, it means it's REDIRECTING!
        print(f"Status Code: {response.status_code}")
        
        # Only assert if the status is 200
        self.assertEqual(response.status_code, 200)

    # 3. Test Forum Access Control (Security Check)
    def test_forum_visitor_restriction(self):
        # Mocking a Visitor role (role 4)
        with self.client.session_transaction() as sess:
            sess['role'] = 4
        
        response = self.client.post('/forum', 
                                    data={'content': 'Hello'}, 
                                    content_type='application/x-www-form-urlencoded',
                                    follow_redirects=True)
        
        # Matches the Access Denied message for non-student roles
        self.assertIn(b"Access Denied: Visitors are limited to VIEW-ONLY access.", response.data)

if __name__ == "__main__":
     unittest.main()
