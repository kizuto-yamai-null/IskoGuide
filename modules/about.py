# modules/about.py
from mock_data import about_assets

class AboutModule:
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 2: BUSINESS LOGIC LAYER
    This module handles data parsing, transformation, and string cleansing for 
    the institutional profile and contact datasets. It reads raw data structures from 
    Layer 3 (mock_data.py) and formats them into exact UI payloads for Layer 1 (views.py).
    """
    def __init__(self):
        self.metadata = about_assets

    def show_School_Credits(self) -> dict:
        """Returns institutional links and core descriptive profile tokens."""
        # 🛡️ TYPE GUARD: Defensive data lookup type assertions to isolate runtime risks
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
        # 🛡️ TYPE GUARD: Uses explicit datatype checks and fallbacks to securely isolate runtime errors
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
    