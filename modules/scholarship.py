# modules/scholarship.py

class ScholarshipModule:
    def __init__(self):
        self.grant_List = []
        self.timelines = []

    def list_Available_Grants(self) -> list: 
        return self.grant_List

    def check_Eligibility(self, gwa: float): 
        pass

    def get_Scholarships_FAQ(self): 
        pass

    def show_Timelines(self) -> list: 
        return self.timelines