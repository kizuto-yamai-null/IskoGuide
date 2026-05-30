# modules/admission.py
import sys
from pathlib import Path
# Allows importing from the parent directory if not running as a package
sys.path.append(str(Path(__file__).resolve().parent.parent))

from mock_data import admission_steps

def show_Enrollment_Guide():
    print("--- PUP Freshman Enrollment Checklist ---")
    for index, step in enumerate(admission_steps, 1):
        print(f"{index}. {step}")

# Example usage:
if __name__ == "__main__":
    show_Enrollment_Guide()