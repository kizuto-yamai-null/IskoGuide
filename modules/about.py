# modules/about.py

class AboutModule:
    def __init__(self):
        self.school_Desc = ""
        self.social_Links = ""

    def show_School_Credits(self) -> str: 
        return self.school_Desc

    def show_Campus_Contacts(self) -> str: 
        return self.social_Links