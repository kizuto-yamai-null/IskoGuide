# mock_data.py

# ==============================================================================
# 1. CAMPUS TOURISM & DIRECTORY LANDMARKS (modules/directory.py)
# 7 landmarks with name, location, description, and search keyword tags
# ==============================================================================
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

# ==============================================================================
# 2. STUDENT SHOP LOCATIONS (modules/directory.py)
# Formatted with name, type of service, location, description, and search keyword tags
# ==============================================================================
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

# ==============================================================================
# 3. UPGRADED ADMISSIONS MODULE DATA LAYOUT (modules/admission.py)
# Trimmed Matrix: Exactly 4 high-priority tracking requirements per student track
# ==============================================================================
admission_requirements_matrix = {
    "Freshman": [
        "Original copy of SAR Form (PUP iApply Enrollment Voucher)",
        "Original copy of Grade 12 Report Card (Form 138)",
        "Original copy of PSA Birth Certificate",
        "Original copy of Certificate of Good Moral Character (with dry seal)"
    ],
    "Transferee": [
        "Certified True Copy of Honorable Dismissal / Transfer Credentials",
        "Official Transcript of Records (TOR) or Informative Copy of Grades",
        "Original copy of PSA Birth Certificate",
        "Certificate of Good Moral Character from previous university"
    ],
    "Returnee": [
        "Approved and signed Application for Readmission Form",
        "PUP Student Academic Record (SAR) evaluation printout",
        "University Clearance Form (Library, Accounting, and Registrar)",
        "PUP Student ID Card for status reactivation tracking"
    ]
}

# ==============================================================================
# 4. ABOUT MODULE ASSETS (modules/about.py)
# Expanded Matrix: Includes social media handles, official administrative helpdesks, and hotlines
# ==============================================================================
about_assets = {
    "website": "pup.edu.ph",
    "social_media": {
        "twitter": "@ThePUPOfficial",
        "linkedin": "PUP Official",
        "facebook": "Polytechnic University of the Philippines"
    },
    # 🏢 Direct communication desks pulled from official university contact nodes
    "helpdesks": [
        {
            "office": "PUP Office of the University Registrar",
            "email": "registrar@pup.edu.ph",
            "hotline": "(632) 5335-1787 local 6285",
            "location": "Main Campus, Ground Floor South Wing"
        },
        {
            "office": "PUP Admission Services Desk",
            "email": "admissions@pup.edu.ph",
            "hotline": "(632) 5335-1787 local 6287 or 6322",
            "location": "Main Campus, Ground Floor East Wing"
        },
        {
            "office": "PUP Medical Clinic / Health Services",
            "email": "medical@pup.edu.ph",
            "hotline": "(632) 5335-1777",
            "location": "Main Campus, East Wing Grounds"
        }
    ]
}

# ==============================================================================
# 5. SCHOLARSHIP & FINANCIAL ASSISTANCE ASSETS (modules/scholarship.py)
# Expanded to support dynamic evaluation criteria for government and university grants
# ==============================================================================
scholarship_guidelines_text = (
    "PUP Scholarship and Financial Assistance channels are open to regularly enrolled "
    "undergraduate students. Applicants must maintain academic GWA caps and meet domestic "
    "household income constraints specific to their government or institutional grant. "
    "Dual-availment of national government funds is strictly monitored."
)

scholarship_deadlines_matrix = {
    "Tulong Dunong Program (TDP)": "First Friday of the Academic Semester",
    "University Merit Scholarship": "Prior to the official Midterm Examination period",
    "DOST-SEI Undergraduate Scholarship": "November 21, 2026"
}