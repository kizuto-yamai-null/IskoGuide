# modules/about.py
from mock_data import about_assets

class AboutModule:
    def __init__(self):
        # Establish reference to the centralized assets dictionary
        self.metadata = about_assets

    def show_School_Credits(self):
        """Returns institutional links and core descriptive profile tokens."""
        return {
            "description": "The Polytechnic University of the Philippines is a premier state university committed to providing inclusive and high-quality technological and professional education.",
            "website": self.metadata.get("website", "pup.edu.ph")
        }

    def show_Campus_Contacts(self):
        """
        Extracts both the social media platform handles AND the newly added 
        official administrative phone numbers/emails for frontend rendering.
        """
        contacts_package = {
            "socials": [],
            "offices": self.metadata.get("helpdesks", [])  # ◄ Unpacks the fixed desk lists safely
        }
        
        # Loop through and structure social channels safely
        socials = self.metadata.get("social_media", {})
        for platform, handle in socials.items():
            contacts_package["socials"].append({
                "channel": platform.capitalize(),
                "address": handle
            })
            
        return contacts_package