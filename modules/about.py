# modules/about.py
from mock_data import about_assets

class AboutModule:
    def __init__(self):
        self.metadata = about_assets

    def show_School_Credits(self):
        """Returns institutional links and core descriptive profile tokens."""
        return {
            "description": "The Polytechnic University of the Philippines is a premier state university committed to providing inclusive and high-quality technological and professional education.",
            "website": self.metadata.get("website", "pup.edu.ph")
        }

    def show_Campus_Contacts(self):
        """Extracts social channels dictionary data from Enrico's data arrays."""
        contacts_table = []
        socials = self.metadata.get("social_media", {})
        
        for platform, handle in socials.items():
            contacts_table.append({
                "channel": platform.capitalize(),
                "address": handle
            })
            
        return contacts_table