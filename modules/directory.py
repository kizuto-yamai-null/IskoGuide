# modules/directory.py
from mock_data import landmarks, student_shops

class CampusDirectory:
    """
    🏢 3-LAYER ARCHITECTURE - LAYER 2: BUSINESS LOGIC LAYER
    This module encapsulates the core textual search algorithms, keyword string parsing,
    and classification rules for campus navigation. It transforms structural datasets 
    from Layer 3 (mock_data.py) into unified, sorted lookup arrays for presentation layers.
    """
    def __init__(self):
        # Master references loaded directly from Enrico's seeded data pool
        self.landmarks_list = landmarks
        self.shops_list = student_shops

    def show_Landmarks(self):
        """Returns the complete array of campus tourist and landmarks data."""
        return self.landmarks_list

    def get_Shop_Locations(self):
        """Returns the full list of local student facilities and services."""
        return self.shops_list

    def search_campus_directory(self, query_string):
        """
        Upgraded Search Engine: Scans names, descriptions, AND 
        custom keyword tags case-insensitively.
        """
        clean_query = query_string.lower().strip()
        if not clean_query:
            return []

        matches = []
        
        # Scan landmarks
        for item in self.landmarks_list:
            if (clean_query in item["name"].lower() or 
                clean_query in item["description"].lower() or 
                any(clean_query in tag for tag in item.get("keywords", []))):
                
                matches.append({"type": "Landmark", "name": item["name"], "info": f"{item['location']} - {item['description']}"})
                
        # Scan shops
        for shop in self.shops_list:
            if (clean_query in shop["name"].lower() or 
                clean_query in shop["description"].lower() or 
                any(clean_query in tag for tag in shop.get("keywords", []))):
                
                matches.append({"type": "Shop/Service", "name": shop["name"], "info": f"[{shop['type_of_service']}] {shop['location']} - {shop['description']}"})

        return matches
    