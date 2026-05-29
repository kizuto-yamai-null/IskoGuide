# modules/directory.py

class CampusDirectory:
    def __init__(self):
        """
        Initializes the Campus Directory Engine.
        """
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Enrico will assign the imported arrays from mock_data.py here.
        # Max 7 Landmarks: {"name", "location", "description"}
        # Max 5 Local Shops: {"name", "type_of_service", "location", "description"}
        # ==============================================================================
        self.landmarks = []
        self.local_Shops = []

    def show_Landmarks(self) -> list: 
        return self.landmarks

    def get_Shop_Locations(self) -> list: 
        return self.local_Shops

    # ==============================================================================
    # 🧠 LEAD ARCHITECT LOGIC (66%): EVALUATION ENGINE
    # ==============================================================================
    def show_Landmark_Details(self, landmark_name: str) -> dict:
        """Finds a specific landmark object, ignoring casing errors."""
        if not landmark_name:
            return {"error": "No landmark name provided", "status": 400}
        clean_name = landmark_name.strip().lower()
        for item in self.landmarks:
            if item["name"].lower() == clean_name:
                return item
        return {"error": f"Landmark '{landmark_name}' not found", "status": 404}

    def get_Shop_Details(self, shop_name: str) -> dict:
        """Finds a specific shop object, ignoring casing errors."""
        if not shop_name:
            return {"error": "No shop name provided", "status": 400}
        clean_name = shop_name.strip().lower()
        for shop in self.local_Shops:
            if shop["name"].lower() == clean_name:
                return shop
        return {"error": f"Shop '{shop_name}' not found", "status": 404}

    def search_campus_directory(self, query: str) -> dict:
        """Performs partial keyword matching across clean, data-agnostic attributes."""
        if not query or not query.strip():
            return {"landmarks": [], "shops": []}
            
        clean_query = query.strip().lower()
        
        matched_landmarks = [
            item for item in self.landmarks 
            if clean_query in item.get("name", "").lower() or clean_query in item.get("location", "").lower()
        ]
        
        matched_shops = [
            shop for shop in self.local_Shops 
            if clean_query in shop.get("name", "").lower() or 
               clean_query in shop.get("location", "").lower() or 
               clean_query in shop.get("type_of_service", "").lower()
        ]
        
        return {
            "landmarks": matched_landmarks,
            "shops": matched_shops
        }