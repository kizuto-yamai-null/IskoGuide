# modules/about.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from mock_data import about_assets

def display_university_info():
    print("--- About Polytechnic University of the Philippines ---")
    print(f"Official Website: {about_assets['website']}")
    print("Social Media Handles:")
    for platform, handle in about_assets['social_media'].items():
        print(f"  - {platform.capitalize()}: {handle}")

# Example usage:
if __name__ == "__main__":
    display_university_info()