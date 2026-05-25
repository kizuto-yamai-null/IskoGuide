# modules/forum.py

class ForumModule:
    def __init__(self):
        self.student_Posts = []
        self.active_Threads = 0

    def create_Post(self, content: str): 
        pass

    def view_threads(self) -> list: 
        return self.student_Posts

    def report_Post(self, postID: int): 
        pass