"""
Static dataset of 50 mock VJTI Computer Engineering students.
All data is hard-coded and deterministic — no randomness at runtime.
"""

MOCK_STUDENTS = [
    # --- App Dev Students ---
    {"name": "Aakash Sharma",   "year": 2, "interest": "AppDev", "leetcode": 320, "cf_rating": 0,    "github_repos": 8,  "projects": ["E-Commerce App", "Weather App"],           "flutter_projects": 2},
    {"name": "Priya Nair",      "year": 2, "interest": "AppDev", "leetcode": 180, "cf_rating": 0,    "github_repos": 5,  "projects": ["Todo App"],                                "flutter_projects": 1},
    {"name": "Rohan Kulkarni",  "year": 3, "interest": "AppDev", "leetcode": 420, "cf_rating": 0,    "github_repos": 12, "projects": ["Health Tracker", "Food Delivery", "Notes"], "flutter_projects": 3},
    {"name": "Sneha Patil",     "year": 2, "interest": "AppDev", "leetcode": 90,  "cf_rating": 0,    "github_repos": 3,  "projects": [],                                          "flutter_projects": 0},
    {"name": "Arjun Mehta",     "year": 2, "interest": "AppDev", "leetcode": 260, "cf_rating": 0,    "github_repos": 7,  "projects": ["Sign Language Detection", "Campus Map"],   "flutter_projects": 2},
    {"name": "Isha Desai",      "year": 3, "interest": "AppDev", "leetcode": 350, "cf_rating": 0,    "github_repos": 10, "projects": ["Women Safety App", "Chat App", "Wallet"],  "flutter_projects": 3},
    {"name": "Vivek Joshi",     "year": 2, "interest": "AppDev", "leetcode": 145, "cf_rating": 0,    "github_repos": 4,  "projects": ["Calculator App"],                          "flutter_projects": 1},
    {"name": "Neha Gokhale",    "year": 4, "interest": "AppDev", "leetcode": 600, "cf_rating": 0,    "github_repos": 18, "projects": ["Fintech App", "AR Navigation", "Edu App", "Portfolio"], "flutter_projects": 4},
    {"name": "Karan Shetty",    "year": 2, "interest": "AppDev", "leetcode": 200, "cf_rating": 0,    "github_repos": 6,  "projects": ["Music Player"],                            "flutter_projects": 1},
    {"name": "Ankita Rane",     "year": 3, "interest": "AppDev", "leetcode": 310, "cf_rating": 0,    "github_repos": 9,  "projects": ["Library App", "Bus Tracker"],              "flutter_projects": 2},
    {"name": "Saurabh Tiwari",  "year": 2, "interest": "AppDev", "leetcode": 50,  "cf_rating": 0,    "github_repos": 2,  "projects": [],                                          "flutter_projects": 0},
    {"name": "Divya Pillai",    "year": 4, "interest": "AppDev", "leetcode": 500, "cf_rating": 0,    "github_repos": 15, "projects": ["Smart Home", "IOT Dashboard", "React Native App"], "flutter_projects": 3},

    # --- Web Dev Students ---
    {"name": "Mihail Gaikwad",  "year": 2, "interest": "WebDev", "leetcode": 200, "cf_rating": 0,    "github_repos": 10, "projects": ["Portfolio Site", "Blog CMS"],             "flutter_projects": 0},
    {"name": "Pooja Iyer",      "year": 2, "interest": "WebDev", "leetcode": 120, "cf_rating": 0,    "github_repos": 7,  "projects": ["E-Commerce"],                             "flutter_projects": 0},
    {"name": "Rahul Deshpande", "year": 3, "interest": "WebDev", "leetcode": 280, "cf_rating": 0,    "github_repos": 14, "projects": ["SaaS Dashboard", "Job Portal", "API"],    "flutter_projects": 0},
    {"name": "Tanvi Bhatt",     "year": 2, "interest": "WebDev", "leetcode": 90,  "cf_rating": 0,    "github_repos": 4,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Yash Pawar",      "year": 2, "interest": "WebDev", "leetcode": 310, "cf_rating": 0,    "github_repos": 9,  "projects": ["React Dashboard", "Chat App"],            "flutter_projects": 0},
    {"name": "Kavya Jain",      "year": 4, "interest": "WebDev", "leetcode": 450, "cf_rating": 0,    "github_repos": 20, "projects": ["Next.js SaaS", "Dev Tools", "Open Source"], "flutter_projects": 0},
    {"name": "Sumit Walke",     "year": 2, "interest": "WebDev", "leetcode": 155, "cf_rating": 0,    "github_repos": 6,  "projects": ["Landing Page"],                           "flutter_projects": 0},
    {"name": "Aishwarya More",  "year": 3, "interest": "WebDev", "leetcode": 230, "cf_rating": 0,    "github_repos": 11, "projects": ["Booking System", "Vue App"],              "flutter_projects": 0},
    {"name": "Pratik Kadam",    "year": 2, "interest": "WebDev", "leetcode": 45,  "cf_rating": 0,    "github_repos": 3,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Shreya Salvi",    "year": 3, "interest": "WebDev", "leetcode": 370, "cf_rating": 0,    "github_repos": 13, "projects": ["HealthTech Portal", "Analytics Dashboard"], "flutter_projects": 0},
    {"name": "Omkar Naik",      "year": 4, "interest": "WebDev", "leetcode": 520, "cf_rating": 0,    "github_repos": 22, "projects": ["Full-Stack CRM", "REST API", "DevOps CI/CD", "Microservices"], "flutter_projects": 0},

    # --- Competitive Programming Students ---
    {"name": "Anish Verma",     "year": 2, "interest": "CP",     "leetcode": 400, "cf_rating": 1450, "github_repos": 3,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Ritika Menon",    "year": 2, "interest": "CP",     "leetcode": 280, "cf_rating": 1200, "github_repos": 2,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Devraj Pandey",   "year": 3, "interest": "CP",     "leetcode": 600, "cf_rating": 1750, "github_repos": 4,  "projects": ["CP Template"],                            "flutter_projects": 0},
    {"name": "Sakshi Chavan",   "year": 2, "interest": "CP",     "leetcode": 150, "cf_rating": 900,  "github_repos": 1,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Nikhil Sawant",   "year": 2, "interest": "CP",     "leetcode": 500, "cf_rating": 1600, "github_repos": 5,  "projects": ["Algorithm Visualizer"],                   "flutter_projects": 0},
    {"name": "Gauri Thakur",    "year": 3, "interest": "CP",     "leetcode": 700, "cf_rating": 1900, "github_repos": 3,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Aditya Kulkarni", "year": 4, "interest": "CP",     "leetcode": 900, "cf_rating": 2200, "github_repos": 6,  "projects": ["CF Tracker"],                             "flutter_projects": 0},
    {"name": "Mansi Bapat",     "year": 2, "interest": "CP",     "leetcode": 200, "cf_rating": 1050, "github_repos": 2,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Vaibhav Gole",    "year": 3, "interest": "CP",     "leetcode": 450, "cf_rating": 1550, "github_repos": 3,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Prachi Doshi",    "year": 2, "interest": "CP",     "leetcode": 330, "cf_rating": 1300, "github_repos": 2,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Harsh Mhatre",    "year": 4, "interest": "CP",     "leetcode": 800, "cf_rating": 2000, "github_repos": 4,  "projects": ["Contest Prep Sheet"],                     "flutter_projects": 0},
    {"name": "Tejal Raut",      "year": 2, "interest": "CP",     "leetcode": 120, "cf_rating": 800,  "github_repos": 1,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Siddesh Lotlikar","year": 3, "interest": "CP",     "leetcode": 560, "cf_rating": 1680, "github_repos": 3,  "projects": [],                                         "flutter_projects": 0},

    # --- AI / ML Students ---
    {"name": "Aanya Singh",     "year": 2, "interest": "AI",     "leetcode": 250, "cf_rating": 0,    "github_repos": 6,  "projects": ["Sign Language Detection"],                "flutter_projects": 0},
    {"name": "Kunal Bhosale",   "year": 2, "interest": "AI",     "leetcode": 180, "cf_rating": 0,    "github_repos": 4,  "projects": ["Face Recognition"],                       "flutter_projects": 0},
    {"name": "Riya Chauhan",    "year": 3, "interest": "AI",     "leetcode": 320, "cf_rating": 0,    "github_repos": 10, "projects": ["Sentiment Analysis", "Stock Predictor", "Object Detection"], "flutter_projects": 0},
    {"name": "Tejas Apte",      "year": 2, "interest": "AI",     "leetcode": 90,  "cf_rating": 0,    "github_repos": 2,  "projects": [],                                         "flutter_projects": 0},
    {"name": "Smita Kale",      "year": 4, "interest": "AI",     "leetcode": 480, "cf_rating": 0,    "github_repos": 16, "projects": ["NLP Classifier", "Recommendation Engine", "CV Pipeline", "Research Paper"], "flutter_projects": 0},
    {"name": "Omkar Patil",     "year": 2, "interest": "AI",     "leetcode": 310, "cf_rating": 0,    "github_repos": 7,  "projects": ["House Price Predictor", "Chatbot"],       "flutter_projects": 0},
    {"name": "Vrinda Lele",     "year": 3, "interest": "AI",     "leetcode": 220, "cf_rating": 0,    "github_repos": 8,  "projects": ["Image Classifier", "Data Pipeline"],      "flutter_projects": 0},
    {"name": "Atharv Shinde",   "year": 2, "interest": "AI",     "leetcode": 140, "cf_rating": 0,    "github_repos": 3,  "projects": ["Linear Regression"],                      "flutter_projects": 0},
    {"name": "Mrunal Gawde",    "year": 4, "interest": "AI",     "leetcode": 550, "cf_rating": 0,    "github_repos": 19, "projects": ["Generative Art", "GAN", "Pose Estimation", "Kaggle Top 10%"], "flutter_projects": 0},
    {"name": "Parth Joshi",     "year": 2, "interest": "AI",     "leetcode": 200, "cf_rating": 0,    "github_repos": 5,  "projects": ["K-Means Clustering"],                     "flutter_projects": 0},
    {"name": "Simran Waghmare", "year": 3, "interest": "AI",     "leetcode": 380, "cf_rating": 0,    "github_repos": 11, "projects": ["Medical Image Seg", "Time-Series Forecast"], "flutter_projects": 0},
    {"name": "Aniket Nagare",   "year": 2, "interest": "AI",     "leetcode": 60,  "cf_rating": 0,    "github_repos": 2,  "projects": [],                                         "flutter_projects": 0},
]
