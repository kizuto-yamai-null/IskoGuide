import unittest
from modules.forum import ForumModule

class TestForumModule(unittest.TestCase):
    
    def setUp(self):
        # Initialize a fresh instance for every test to ensure data isolation
        self.forum = ForumModule()

    # --- SECURITY TESTS ---
    def test_profanity_filter(self):
        # Test clean content
        self.assertFalse(self.forum.check_for_spam("Hello, this is a clean post!"))
        # Test flagged content
        self.assertTrue(self.forum.check_for_spam("This is a puta test"))

    # --- WORKFLOW TESTS ---
    def test_post_lifecycle(self):
        # 1. Create a post
        success, message = self.forum.create_Post("Kyla", "OOP Project", "Testing logic.")
        self.assertTrue(success)
        self.assertEqual(len(self.forum.get_pending_queue()), 1)

        # 2. Approve the post
        post_id = self.forum.get_pending_queue()[0]["post_id"]
        approve_success = self.forum.approve_post(post_id)
        self.assertTrue(approve_success)
        
        # Updated: 1 (Welcome post) + 1 (New post) = 2
        self.assertEqual(len(self.forum.view_threads()), 2) 
        self.assertEqual(len(self.forum.get_pending_queue()), 0)

        # 3. Report the post
        # Updated: 2 total posts - 1 reported = 1 remaining
        report_success = self.forum.report_Post(post_id)
        self.assertTrue(report_success)
        self.assertEqual(len(self.forum.view_threads()), 1)

    # --- BONUS POINT TEST ---
    def test_reject_post(self):
        # Create a post
        self.forum.create_Post("User", "Title", "Content")
        post_id = self.forum.get_pending_queue()[0]["post_id"]
        
        # Test rejection
        success = self.forum.reject_post(post_id)
        self.assertTrue(success)
        self.assertEqual(len(self.forum.get_pending_queue()), 0, "Post should be removed from queue")

if __name__ == '__main__':
     unittest.main()
