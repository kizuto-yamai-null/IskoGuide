import unittest
from unittest.mock import patch
from modules.about import AboutModule

class TestAboutModule(unittest.TestCase):
    
    def setUp(self):
        self.about = AboutModule()

    # 1. Happy Path: Verify standard data extraction works
    def test_show_school_credits_success(self):
        result = self.about.show_School_Credits()
        self.assertIsInstance(result, dict)
        self.assertIn("description", result)
        self.assertIn("website", result)

    # 2. Resilience: Force empty data and verify fallbacks work
    def test_show_campus_contacts_with_empty_data(self):
        with patch('modules.about.about_assets', {}):
            about_empty = AboutModule() 
            result = about_empty.show_Campus_Contacts()
            
            self.assertEqual(result["socials"], [])
            self.assertEqual(result["offices"], [])

    # 3. Defensive Programming: Verify that invalid types return empty fallbacks (no crash!)
    def test_invalid_data_type_handling(self):
        # We manually inject bad data (a string instead of a dict)
        self.about.metadata = "This is not a dictionary"
        
        # Now we assert that the function returns the fallback structure 
        # instead of raising an exception.
        result = self.about.show_Campus_Contacts()
        
        self.assertEqual(result, {"socials": [], "offices": []})

if __name__ == '__main__':
    unittest.main()