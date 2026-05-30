# mock_data.py

# 1. Campus Tourism & Directory Landmarks (modules/directory.py)
# 7 landmarks with name, location, description, and search keyword tags
landmarks = [
    {
        "name": "The Pylon",
        "location": "Main Campus Entrance, Anonas Street",
        "description": "The iconic tri-columnar structure representing the university's triad of truth, excellence, and wisdom.",
        "keywords": ["pylon", "entrance", "gate", "anonas", "pillars", "triad", "wisdom"]
    },
    {
        "name": "Oval",
        "location": "East Wing, Main Campus Grounds",
        "description": "The central athletic grounds used for sports events, physical education classes, and student assemblies.",
        "keywords": ["oval", "sports", "pe", "takbo", "field", "athletic", "ground", "daan"]
    },
    {
        "name": "Obelisk",
        "location": "Main Building Courtyard",
        "description": "A historic monument standing tall as a symbol of the university's enduring strength and resilience.",
        "keywords": ["obelisk", "courtyard", "monument", "statue", "center", "main building"]
    },
    {
        "name": "Ninoy Aquino Learning Resources Center",
        "location": "Central Campus Block",
        "description": "The main university library housing vast academic collections, research archives, and quiet study spaces.",
        "keywords": ["library", "ninoy aquino", "lrc", "libro", "books", "study", "quiet", "aircon", "research"]
    },
    {
        "name": "Multi-Purpose Building (Gymnasium)",
        "location": "Adjacent to the Oval",
        "description": "An indoor sports arena and venue for major university convocations, cultural events, and graduation rites.",
        "keywords": ["gym", "gymnasium", "mpb", "basketball", "grad", "graduation", "event", "stage"]
    },
    {
        "name": "Inter-Faith Chapel",
        "location": "Main Campus Garden Area",
        "description": "A quiet, inclusive space dedicated to spiritual reflection and multi-denominational services for the community.",
        "keywords": ["chapel", "church", "dasal", "pray", "interfaith", "quiet", "mass", "spiritual"]
    },
    {
        "name": "Linear Park",
        "location": "Pasig Riverfront, Main Campus",
        "description": "A scenic, open-air walkway by the riverbank ideal for student relaxation, group studies, and leisure.",
        "keywords": ["park", "linear", "ilog", "pasig river", "tambayan", "hangout", "upo", "relax", "walkway"]
    }
]

# 2. Student Shop Locations (modules/directory.py)
# Formatted with name, type of service, location, description, and search keyword tags
student_shops = [
    {
        "name": "Lagoon Food Stalls",
        "type_of_service": "Food and Beverage",
        "location": "PUP Lagoon Area",
        "description": "Affordable meals, snacks, and street food options tailored to a student's daily budget.",
        "keywords": ["lagoon", "food", "kain", "lunch", "snacks", "budget", "tusok-tusok", "siomai", "rice", "uulam"]
    },
    {
        "name": "Full Cup",
        "type_of_service": "Cafeteria and Study Space",
        "location": "PUP Ninoy Aquino Library and Learning Resources Center",
        "description": "A cozy in-library coffee spot serving beverages and light refreshments for studying students.",
        "keywords": ["full cup", "coffee", "cafe", "study", "library", "kape", "drinks", "snacks"]
    },
    {
        "name": "School Supplies and Printing Shops",
        "type_of_service": "Printing and Stationery",
        "location": "Main Building Ground Floor / Sub-Station",
        "description": "Offers document printing, photocopying, bookbinding, and essential school supplies.",
        "keywords": ["print", "photocopy", "xerox", "binding", "ballpen", "papel", "school supplies", "stationery"]
    },
    {
        "name": "Souvenir Shop",
        "type_of_service": "Retail / Merchandise",
        "location": "Main Campus Visitor Center",
        "description": "The official hub for university-branded apparel, jackets, lanyards, and PUP memorabilia.",
        "keywords": ["souvenir", "merch", "shirt", "lanyard", "id", "jacket", "pup gear", "items", "bili"]
    }
]

# (Keep Enrico's exact admission_steps and about_assets lists down below unchanged)
admission_steps = ["Original copy of SAR Form","Original copy of CTC of Grade 10 and 11 Report Cards","Original copy of Grade 12 Report Card","Original copy of PSA Birth Certificate","Original copy of Good Moral Certificate (with dry seal)","Original copy of Oath of Undertaking / Waiver","Original copy of Route & Approval Slip","Original copy of Health Information Form","Chest X-ray film or printed result (must be dated within 6 months prior to enrollment)"]
about_assets = {"website": "pup.edu.ph","social_media": {"twitter": "@ThePUPOfficial","linkedin": "PUP Official","facebook": "Polytechnic University of the Philippines"}}