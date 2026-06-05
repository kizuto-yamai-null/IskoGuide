# modules/about.py
from mock_data import about_assets

class AboutModule:
    def __init__(self):
        self.metadata = about_assets

    def show_School_Credits(self) -> dict:
        """Returns institutional links and core descriptive profile tokens."""
        # 🛠️ FIXED: Defensive data lookup type assertions
        if not isinstance(self.metadata, dict):
            return {"description": "Information temporarily unavailable.", "website": "pup.edu.ph"}
            
        return {
            "description": "The Polytechnic University of the Philippines is a premier state university committed to providing inclusive and high-quality technological and professional education.",
            "website": self.metadata.get("website", "pup.edu.ph")
        }

    def show_Campus_Contacts(self) -> dict:
        """
        Extracts social media metadata platform arrays and packages structured helpdesk tables.
        """
        # 🛠️ FIXED: Uses explicit datatype checks and fallbacks to securely isolate runtime errors
        is_valid_data = isinstance(self.metadata, dict)
        
        contacts_package = {
            "socials": [],
            "offices": self.metadata.get("helpdesks", []) if is_valid_data else []
        }
        
        socials_map = self.metadata.get("social_media", {}) if is_valid_data else {}
        
        # Guard against malformed dictionary properties safely
        if isinstance(socials_map, dict):
            for platform, handle in socials_map.items():
                contacts_package["socials"].append({
                    "channel": platform.capitalize(),
                    "address": handle
                })
            
        return contacts_package
    