# modules/directory.py

class CampusDirectory:
    def __init__(self):
        self.landmarks = []
        self.local_Shops = []

    def show_Landmarks(self) -> list: 
        return self.landmarks

    def show_Landmark_Details(self, landmarkName: str): 
        pass

    def get_Shop_Locations(self) -> list: 
        return self.local_Shops

    def get_Shop_Details(self, shopName: str): 
        pass