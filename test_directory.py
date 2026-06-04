import unittest
from modules.directory import CampusDirectory

class TestCampusDirectory(unittest.TestCase):
    
    def setUp(self):
        # Initialize the module before each test
        self.directory = CampusDirectory()

    # 1. Test data loading
    def test_data_loading(self):
        landmarks = self.directory.show_Landmarks()
        shops = self.directory.get_Shop_Locations()
        self.assertGreater(len(landmarks), 0, "Landmarks should be loaded")
        self.assertGreater(len(shops), 0, "Shops should be loaded")

    # 2. Test search functionality (Case Insensitive)
    def test_search_keywords(self):
        # Searching for "Library" (found in keyword tags)
        results = self.directory.search_campus_directory("library")
        self.assertGreater(len(results), 0, "Should find results for 'library'")
        
        # Check if one of the results is the Ninoy Aquino Learning Resources Center
        names = [item["name"] for item in results]
        self.assertIn("Ninoy Aquino Learning Resources Center", names)

    # 3. Test empty query (Graceful Handling)
    def test_empty_query(self):
        results = self.directory.search_campus_directory("")
        self.assertEqual(results, [], "Empty query should return empty list")

    # 4. Test non-existent item
    def test_no_matches(self):
        results = self.directory.search_campus_directory("asdfghjkl123")
        self.assertEqual(results, [], "Non-existent query should return empty list")

if __name__ == '__main__':
    unittest.main()