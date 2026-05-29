# modules/directory.py

class CampusDirectory:
    def __init__(self):
        """
        Initializes the Campus Directory Engine.
        """
        # ==============================================================================
        # 📝 ENRICO'S TASK (33%): DATA SEEDING & STATIC TEXT DATA POOL
        # Populate these lists with granular data cards (including stall_number, items, etc.).
        # ==============================================================================
        self.landmarks = [
            {
                "name": "Mabini Obelisk",
                "zone": "Main Campus - Center",
                "desc": "The prominent monument located right at the heart of the Mabini Campus.",
                "details": "Situated in front of the Main Academic Building."
            },
            {
                "name": "PUP Pylon",
                "zone": "Main Campus - Entrance",
                "desc": "The towering triangular pillar structure greeting everyone at the main gates.",
                "details": "Symbolizes truth, excellence, and wisdom."
            }
        ]
        
        self.local_Shops = [
            {
                "name": "PUP Lagoon Food Stalls",
                "type": "Food & Dining",
                "location": "Mabini Campus - Near Inner Court",
                "stall_number": "Stall #08",
                "desc": "The iconic budget eating hub famous for student meals.",
                "featured_items": ["Siomai Rice", "Sisig Rice"]
            }
        ]

    def show_Landmarks(self) -> list: 
        return self.landmarks

    def get_Shop_Locations(self) -> list: 
        return self.local_Shops

    # ==============================================================================
    # 🧠 LEAD ARCHITECT LOGIC (66%): EVALUATION ENGINE
    # ==============================================================================
    def show_Landmark_Details(self, landmark_name: str) -> dict:
        """Finds and returns a specific landmark object, ignoring casing errors."""
        if not landmark_name:
            return {"error": "No landmark name provided", "status": 400}
        clean_name = landmark_name.strip().lower()
        for item in self.landmarks:
            if item["name"].lower() == clean_name:
                return item
        return {"error": f"Landmark '{landmark_name}' not found", "status": 404}

    def get_Shop_Details(self, shop_name: str) -> dict:
        """Finds and returns a specific shop object, ignoring casing errors."""
        if not shop_name:
            return {"error": "No shop name provided", "status": 400}
        clean_name = shop_name.strip().lower()
        for shop in self.local_Shops:
            if shop["name"].lower() == clean_name:
                return shop
        return {"error": f"Shop '{shop_name}' not found", "status": 404}

    def search_campus_directory(self, query: str) -> dict:
        """
        Performs structural filtering loops across landmarks and shops.
        """
        if not query or not query.strip():
            return {"landmarks": [], "shops": []}
            
        clean_query = query.strip().lower()
        
        matched_landmarks = [
            item for item in self.landmarks 
            if clean_query in item["name"].lower() or clean_query in item["zone"].lower()
        ]
        
        matched_shops = [
            shop for shop in self.local_Shops 
            if clean_query in shop["name"].lower() or 
               clean_query in shop["location"].lower() or 
               any(clean_query in item.lower() for item in shop.get("featured_items", []))
        ]
        
        return {
            "landmarks": matched_landmarks,
            "shops": matched_shops
        }