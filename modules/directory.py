# modules/directory.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from mock_data import landmarks, student_shops

def get_Shop_Details(shop_name):
    """
    Scans through the mock student shop array and returns 
    details for the matching shop key.
    """
    # Clean the query for case-insensitive matching
    query = shop_name.lower().strip()
    
    for shop in student_shops:
        if query in shop["name"].lower():
            return shop
            
    return {"error": f"Shop '{shop_name}' not found in the directory."}

# Example usage:
if __name__ == "__main__":
    # Test lookup
    details = get_Shop_Details("Full Cup")
    print(details)