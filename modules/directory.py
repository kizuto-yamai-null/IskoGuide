# modules/directory.py
from mock_data import landmarks, student_shops

class CampusDirectory:
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
        Enrico's logic upgraded: Case-insensitive search filter that returns 
        matching items from both landmarks and local consumer shops.
        """
        clean_query = query_string.lower().strip()
        if not clean_query:
            return []

        matches = []
        
        # Scan landmarks
        for item in self.landmarks_list:
            if clean_query in item["name"].lower() or clean_query in item["description"].lower():
                matches.append({"type": "Landmark", "name": item["name"], "info": f"{item['location']} - {item['description']}"})
                
        # Scan shops
        for shop in self.shops_list:
            if clean_query in shop["name"].lower() or clean_query in shop["description"].lower():
                matches.append({"type": "Shop/Service", "name": shop["name"], "info": f"[{shop['type_of_service']}] {shop['location']} - {shop['description']}"})

        return matches