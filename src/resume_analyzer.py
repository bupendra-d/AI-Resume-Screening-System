import re

# 1) Word Count
def count_words(text: str) -> int:
    """
    Count the total number of words in a resume.
    """

    words = re.findall(r"\b\w+\b", text)

    return len(words)



# 2) Email Detection
def detect_email(text: str):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None



# 3) Phone Detection
def detect_phone(text: str):

    pattern = r"\+?\d[\d\s().-]{7,}\d"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None



# 4) Linked-In Detection
def detect_linkedin(text: str):

    pattern = r"(linkedin\.com/[^\s]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None



# 5) GitHub Detection
def detect_github(text: str):

    pattern = r"(github\.com/[^\s]+)"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None



# 6) Education Detection
def detect_education(text: str):

    education_levels = [
        "PhD",
        "Doctorate",
        "Master",
        "M.Tech",
        "M.E",
        "MBA",
        "MCA",
        "Bachelor",
        "B.Tech",
        "B.E",
        "B.Sc",
        "B.Com",
        "BBA",
        "BCA",
        "Diploma"
    ]

    for level in education_levels:
        if re.search(rf"\b{re.escape(level)}\b", text, re.IGNORECASE):
            return level

    return None



# 7) Experience Detection
def detect_experience(text: str):

    pattern = r"\b\d+\+?\s*(?:years?|yrs?|yr)\b"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return None



# 8) Skills Detection

# INFORMATION TECHNOLOGY
IT_SKILLS = [
    "Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript",
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle",
    "HTML", "CSS", "React", "Angular", "Vue", "Node.js",
    "Flask", "Django", "FastAPI",
    "Git", "GitHub", "Linux", "Docker", "Kubernetes",
    "AWS", "Azure", "GCP",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "Machine Learning", "Deep Learning", "NLP",
    "Pandas", "NumPy", "OpenCV",
    "Power BI", "Tableau", "Excel", "Spark", "Hadoop"
]


# BUSINESS / SALES
BUSINESS_SKILLS = [
    "Business Development",
    "Lead Generation",
    "Sales",
    "Cold Calling",
    "Negotiation",
    "CRM",
    "Salesforce",
    "HubSpot",
    "Customer Relationship Management",
    "Market Research",
    "Marketing",
    "Digital Marketing",
    "Email Marketing",
    "SEO",
    "SEM",
    "Brand Management",
    "Business Analysis",
    "Client Management",
    "B2B",
    "B2C"
]


# FINANCE / ACCOUNTING / BANKING
FINANCE_SKILLS = [
    "Accounting",
    "Bookkeeping",
    "Financial Analysis",
    "Financial Modeling",
    "Auditing",
    "Taxation",
    "GST",
    "Tally",
    "QuickBooks",
    "SAP",
    "ERP",
    "Accounts Payable",
    "Accounts Receivable",
    "Budgeting",
    "Forecasting",
    "Investment Analysis",
    "Risk Management",
    "Banking",
    "Credit Analysis",
    "Wealth Management",
    "Excel"
]


# HR
HR_SKILLS = [
    "Recruitment",
    "Talent Acquisition",
    "Payroll",
    "Employee Engagement",
    "Performance Management",
    "HRMS",
    "Onboarding",
    "Training",
    "Conflict Resolution",
    "Compensation",
    "Employee Relations"
]


# ADVOCATE / LEGAL
LEGAL_SKILLS = [
    "Legal Research",
    "Legal Drafting",
    "Litigation",
    "Contract Management",
    "Corporate Law",
    "Civil Law",
    "Criminal Law",
    "Legal Compliance",
    "Case Management",
    "Arbitration"
]


# ENGINEERING
ENGINEERING_SKILLS = [
    "AutoCAD",
    "SolidWorks",
    "CATIA",
    "ANSYS",
    "MATLAB",
    "PLC",
    "SCADA",
    "Embedded Systems",
    "Circuit Design",
    "Mechanical Design",
    "Electrical Engineering",
    "Civil Engineering",
    "Project Management",
    "Quality Control"
]


# HEALTHCARE
HEALTHCARE_SKILLS = [
    "Patient Care",
    "Clinical Research",
    "Medical Coding",
    "Medical Billing",
    "Diagnosis",
    "Nursing",
    "Phlebotomy",
    "EMR",
    "EHR",
    "Healthcare Management",
    "BLS",
    "CPR"
]


# TEACHER
TEACHER_SKILLS = [
    "Teaching",
    "Lesson Planning",
    "Curriculum Development",
    "Classroom Management",
    "Assessment",
    "Student Counseling",
    "Online Teaching",
    "Mentoring",
    "Educational Technology"
]


# AVIATION
AVIATION_SKILLS = [
    "Flight Operations",
    "Cabin Crew",
    "Air Traffic Control",
    "Ground Handling",
    "Aviation Safety",
    "Aircraft Maintenance",
    "DGCA",
    "Passenger Service",
    "Crew Resource Management"
]

# CHEF
CHEF_SKILLS = [
    "Food Preparation",
    "Menu Planning",
    "Baking",
    "Pastry",
    "Kitchen Management",
    "Food Safety",
    "Inventory Management",
    "Culinary Arts",
    "Recipe Development"
]


# FITNESS
FITNESS_SKILLS = [
    "Personal Training",
    "Nutrition",
    "Strength Training",
    "Yoga",
    "Cardio",
    "CrossFit",
    "Weight Loss",
    "Fitness Assessment",
    "Exercise Physiology"
]


# CONSTRUCTION
CONSTRUCTION_SKILLS = [
    "Construction Management",
    "Site Supervision",
    "Project Planning",
    "Quantity Surveying",
    "Blueprint Reading",
    "AutoCAD",
    "Safety Management",
    "Surveying"
]


# PUBLIC RELATIONS / MEDIA
MEDIA_SKILLS = [
    "Public Relations",
    "Content Writing",
    "Copywriting",
    "Social Media",
    "Adobe Photoshop",
    "Illustrator",
    "Premiere Pro",
    "After Effects",
    "Canva",
    "Photography",
    "Video Editing",
    "Graphic Design"
]


# DESIGN
DESIGN_SKILLS = [
    "UI Design",
    "UX Design",
    "Figma",
    "Adobe XD",
    "Wireframing",
    "Prototyping",
    "Sketch",
    "Photoshop",
    "Illustrator"
]


# AGRICULTURE
AGRICULTURE_SKILLS = [
    "Crop Management",
    "Soil Testing",
    "Irrigation",
    "Farm Management",
    "Agronomy",
    "Organic Farming",
    "Pest Management"
]

# AUTOMOBILE
AUTOMOBILE_SKILLS = [
    "Vehicle Maintenance",
    "Automotive Repair",
    "Engine Diagnostics",
    "Service Management",
    "Mechanical Repair"
]


# BPO
BPO_SKILLS = [
    "Customer Support",
    "Customer Service",
    "Call Handling",
    "Communication",
    "Technical Support",
    "Problem Solving",
    "Voice Process",
    "Non Voice Process"
]


# CONSULTANT
CONSULTANT_SKILLS = [
    "Consulting",
    "Business Strategy",
    "Process Improvement",
    "Stakeholder Management",
    "Presentation Skills",
    "Problem Solving",
    "Data Analysis"
]


# APPAREL
APPAREL_SKILLS = [
    "Fashion Design",
    "Garment Production",
    "Textile Design",
    "Merchandising",
    "Pattern Making",
    "Retail Management"
]


# MASTER LIST
SKILLS = sorted(set(
    IT_SKILLS +
    BUSINESS_SKILLS +
    FINANCE_SKILLS +
    HR_SKILLS +
    LEGAL_SKILLS +
    ENGINEERING_SKILLS +
    HEALTHCARE_SKILLS +
    TEACHER_SKILLS +
    AVIATION_SKILLS +
    CHEF_SKILLS +
    FITNESS_SKILLS +
    CONSTRUCTION_SKILLS +
    MEDIA_SKILLS +
    DESIGN_SKILLS +
    AGRICULTURE_SKILLS +
    AUTOMOBILE_SKILLS +
    BPO_SKILLS +
    CONSULTANT_SKILLS +
    APPAREL_SKILLS
))


def detect_skills(text: str):
    found_skills = []

    for skill in SKILLS:
        if re.search(
            rf"\b{re.escape(skill)}\b",
            text,
            re.IGNORECASE
        ):
            found_skills.append(skill)

    return found_skills



# 9) Final Resume-Analyzer Function:
def analyze_resume(text: str):

    analysis = {

        "word_count": count_words(text),

        "email": detect_email(text),

        "phone": detect_phone(text),

        "linkedin": detect_linkedin(text),

        "github": detect_github(text),

        "education": detect_education(text),

        "experience": detect_experience(text),

        "skills": detect_skills(text)

    }

    return analysis