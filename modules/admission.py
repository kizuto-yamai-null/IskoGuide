# modules/admission.py

class AdmissionModule:
    def __init__(self):
        self.enrollment_Steps = ""
        self.requirements = []

    def show_Enrollment_Guide(self) -> str: 
        return self.enrollment_Steps

    def list_Requirements(self, gwa: float) -> list: 
        return self.requirements

    def Get_Admission_FAQ(self): 
        pass