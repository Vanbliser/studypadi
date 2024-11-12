export const mockQuiz = {
  'quiz': {
    // Quiz details for the 'Skeletal System'
    'quiz_name': 'Introduction to the Skeletal System',
    'quiz_type': 'pastQ', // Can be 'special' or 'pastQ'
    'duration': 2, // in minutes
    'total_questions': 5,
    'questions': [
        {
            'id': 1,
            'content': 'What is the longest bone in the human body?',
            'options': {
                'A': 'Femur',
                'B': 'Humerus',
                'C': 'Tibia',
                'D': 'Fibula'
            },
            'correct_answer': 'A',
            'difficulty_level': 'medium',
            'question_type': 'mcq'
        },
        {
            'id': 2,
            'content': 'Which of the following is not a part of the axial skeleton?',
            'options': {
                'A': 'Skull',
                'B': 'Vertebral column',
                'C': 'Ribs',
                'D': 'Femur'
            },
            'correct_answer': 'D',
            'difficulty_level': 'easy',
            'question_type': 'mcq'
        },
        {
            'id': 3,
            'content': 'How many ribs does a normal human have?',
            'options': {
                'A': '10',
                'B': '12',
                'C': '24',
                'D': '32'
            },
            'correct_answer': 'C',
            'difficulty_level': 'medium',
            'question_type': 'mcq'
        },
        {
            'id': 4,
            'content': 'Which bone protects the brain?',
            'options': {
                'A': 'Scapula',
                'B': 'Cranium',
                'C': 'Mandible',
                'D': 'Sternum'
            },
            'correct_answer': 'B',
            'difficulty_level': 'easy',
            'question_type': 'mcq'
        },
        {
            'id': 5,
            'content': 'The kneecap is also known as:',
            'options': {
                'A': 'Patella',
                'B': 'Femur',
                'C': 'Tibia',
                'D': 'Radius'
            },
            'correct_answer': 'A',
            'difficulty_level': 'easy',
            'question_type': 'mcq'
        }
    ],
    'instant_correction': true, // Whether to show correct answers immediately after each question
    'created_by': 'Educator123', // Sample educator/user who created the quiz
    'created_at': '2024-10-28T10:00:00Z'
}
};


export const mockData = {
    'modules': [
        'Medicine & Health Sciences',
        'Science & Technology',
        'Engineering',
        'Social Sciences & Humanities',
        'Business & Management',
        'Arts & Literature',
        'Information Technology',
        'Language Learning'
    ],
    'subModules': {
        'Medicine & Health Sciences': [
            'Radiology',
            'Anatomy',
            'Pharmacology',
            'Pathology',
            'Physiology',
            'Nursing'
        ]
    },
    'section': {
        'Anatomy': [
            'Skeletal System',
            'Muscular System',
            'Nervous System',
            'Cardiovascular System',
            'Respiratory System'
        ]
    },
    'quiz': {
        // Quiz details for the 'Skeletal System'
        'quiz_name': 'Introduction to the Skeletal System',
        'quiz_type': 'pastQ', // Can be 'special' or 'pastQ'
        'duration': 30, // in minutes
        'total_questions': 5,
        'questions': [
            {
                'id': 1,
                'content': 'What is the longest bone in the human body?',
                'options': {
                    'A': 'Femur',
                    'B': 'Humerus',
                    'C': 'Tibia',
                    'D': 'Fibula'
                },
                'correct_answer': 'A',
                'difficulty_level': 'medium',
                'question_type': 'mcq'
            },
            {
                'id': 2,
                'content': 'Which of the following is not a part of the axial skeleton?',
                'options': {
                    'A': 'Skull',
                    'B': 'Vertebral column',
                    'C': 'Ribs',
                    'D': 'Femur'
                },
                'correct_answer': 'D',
                'difficulty_level': 'easy',
                'question_type': 'mcq'
            },
            {
                'id': 3,
                'content': 'How many ribs does a normal human have?',
                'options': {
                    'A': '10',
                    'B': '12',
                    'C': '24',
                    'D': '32'
                },
                'correct_answer': 'C',
                'difficulty_level': 'medium',
                'question_type': 'mcq'
            },
            {
                'id': 4,
                'content': 'Which bone protects the brain?',
                'options': {
                    'A': 'Scapula',
                    'B': 'Cranium',
                    'C': 'Mandible',
                    'D': 'Sternum'
                },
                'correct_answer': 'B',
                'difficulty_level': 'easy',
                'question_type': 'mcq'
            },
            {
                'id': 5,
                'content': 'The kneecap is also known as:',
                'options': {
                    'A': 'Patella',
                    'B': 'Femur',
                    'C': 'Tibia',
                    'D': 'Radius'
                },
                'correct_answer': 'A',
                'difficulty_level': 'easy',
                'question_type': 'mcq'
            }
        ],
        'instant_correction': false, // Whether to show correct answers immediately after each question
        'created_by': 'Educator123', // Sample educator/user who created the quiz
        'created_at': '2024-10-28T10:00:00Z'
    }
};

// For easier testing, you can log the mock data to check the structure
console.log(mockData);

export const mockClass = {
    "modules": [
      {
        "id": 1,
        "name": "Medicine & Health Sciences",
        "submodules": [
          {
            "name": "Radiology",
            "sections": [
              "X-ray Imaging",
              "MRI Techniques",
              "Ultrasound Diagnostics",
              "CT Scans",
              "Nuclear Medicine",
              "Interventional Radiology"
            ]
          },
          {
            "name": "Anatomy",
            "sections": [
              "Skeletal System",
              "Muscular System",
              "Nervous System",
              "Cardiovascular System",
              "Respiratory System"
            ]
          },
          {
            "name": "Pharmacology",
            "sections": [
              "Drug Classifications",
              "Pharmacokinetics",
              "Pharmacodynamics",
              "Antibiotics",
              "Pain Management"
            ]
          },
          {
            "name": "Pathology",
            "sections": [
              "Histopathology",
              "Hematology",
              "Clinical Chemistry",
              "Microbiology",
              "Forensic Pathology"
            ]
          },
          {
            "name": "Physiology",
            "sections": [
              "Cellular Physiology",
              "Neurophysiology",
              "Cardiovascular Physiology",
              "Endocrinology",
              "Renal Physiology"
            ]
          },
          {
            "name": "Nursing",
            "sections": [
              "Fundamentals of Nursing",
              "Patient Care Techniques",
              "Nursing Ethics",
              "Critical Care Nursing",
              "Pediatric Nursing"
            ]
          }
        ]
      },
      {
        "id": 2,
        "name": "Science & Technology",
        "submodules": [
          {
            "name": "Computer Science",
            "sections": [
              "Data Structures & Algorithms",
              "Operating Systems",
              "Database Management",
              "Cybersecurity",
              "Artificial Intelligence"
            ]
          },
          {
            "name": "Biology",
            "sections": [
              "Genetics",
              "Cell Biology",
              "Ecology",
              "Evolutionary Biology",
              "Biochemistry"
            ]
          },
          {
            "name": "Physics",
            "sections": [
              "Mechanics",
              "Electromagnetism",
              "Thermodynamics",
              "Quantum Physics",
              "Optics"
            ]
          },
          {
            "name": "Chemistry",
            "sections": [
              "Organic Chemistry",
              "Inorganic Chemistry",
              "Physical Chemistry",
              "Analytical Chemistry",
              "Environmental Chemistry"
            ]
          }
        ]
      },
      {
        "id": 3,
        "name": "Engineering",
        "submodules": [
          {
            "name": "Electrical Engineering",
            "sections": [
              "Circuit Analysis",
              "Signal Processing",
              "Control Systems",
              "Power Electronics",
              "Microelectronics"
            ]
          },
          {
            "name": "Mechanical Engineering",
            "sections": [
              "Thermodynamics",
              "Fluid Mechanics",
              "Machine Design",
              "Heat Transfer",
              "Robotics"
            ]
          },
          {
            "name": "Civil Engineering",
            "sections": [
              "Structural Analysis",
              "Construction Materials",
              "Geotechnical Engineering",
              "Hydraulics",
              "Transportation Engineering"
            ]
          }
        ]
      },
      {
        "id": 4,
        "name": "Social Sciences & Humanities",
        "submodules": [
          {
            "name": "Psychology",
            "sections": [
              "Cognitive Psychology",
              "Developmental Psychology",
              "Clinical Psychology",
              "Social Psychology",
              "Behavioral Therapy"
            ]
          },
          {
            "name": "Sociology",
            "sections": [
              "Social Theories",
              "Family Dynamics",
              "Globalization",
              "Social Stratification",
              "Urban Sociology"
            ]
          },
          {
            "name": "Economics",
            "sections": [
              "Microeconomics",
              "Macroeconomics",
              "International Trade",
              "Econometrics",
              "Development Economics"
            ]
          }
        ]
      },
      {
        "id": 5,
        "name": "Business & Management",
        "submodules": [
          {
            "name": "Marketing",
            "sections": [
              "Digital Marketing",
              "Market Research",
              "Brand Management",
              "Consumer Behavior",
              "Sales Strategy"
            ]
          },
          {
            "name": "Finance",
            "sections": [
              "Financial Accounting",
              "Investment Analysis",
              "Corporate Finance",
              "Risk Management",
              "Personal Finance"
            ]
          },
          {
            "name": "Human Resources",
            "sections": [
              "Recruitment & Selection",
              "Performance Management",
              "Organizational Behavior",
              "Employee Relations",
              "Compensation & Benefits"
            ]
          },
          {
            "name": "Project Management",
            "sections": [
              "Agile Methodologies",
              "Project Planning",
              "Risk Assessment",
              "Resource Management",
              "Quality Control"
            ]
          }
        ]
      },
      {
        "id": 6,
        "name": "Arts & Literature",
        "submodules": [
          {
            "name": "English Literature",
            "sections": [
              "Shakespearean Works",
              "19th Century Novels",
              "Poetry Analysis",
              "Modernist Literature",
              "Literary Criticism"
            ]
          },
          {
            "name": "History",
            "sections": [
              "Ancient Civilizations",
              "World War I & II",
              "African History",
              "Medieval Europe",
              "History of Science"
            ]
          },
          {
            "name": "Philosophy",
            "sections": [
              "Ancient Philosophy",
              "Ethics & Morality",
              "Existentialism",
              "Political Philosophy",
              "Philosophy of Mind"
            ]
          }
        ]
      },
      {
        "id": 7,
        "name": "Information Technology",
        "submodules": [
          {
            "name": "Web Development",
            "sections": [
              "HTML & CSS",
              "JavaScript Frameworks",
              "Front-end vs Back-end",
              "API Integration",
              "Responsive Design"
            ]
          },
          {
            "name": "Data Science",
            "sections": [
              "Data Analysis with Python",
              "Machine Learning Algorithms",
              "Data Visualization",
              "Big Data Technologies",
              "Statistical Modeling"
            ]
          },
          {
            "name": "Networking",
            "sections": [
              "Network Protocols",
              "Cybersecurity Essentials",
              "Wireless Communication",
              "Cloud Computing",
              "Network Troubleshooting"
            ]
          }
        ]
      },
      {
        "id": 8,
        "name": "Language Learning",
        "submodules": [
          {
            "name": "French",
            "sections": [
              "Basic Vocabulary",
              "French Grammar",
              "Conversation Skills",
              "French Culture & History",
              "Advanced Reading Comprehension"
            ]
          },
          {
            "name": "Spanish",
            "sections": [
              "Common Phrases",
              "Verb Conjugations",
              "Spanish Literature",
              "Listening Comprehension",
              "Business Spanish"
            ]
          },
          {
            "name": "Mandarin Chinese",
            "sections": [
              "Pinyin & Pronunciation",
              "Writing Characters",
              "Mandarin Grammar",
              "Chinese Idioms",
              "Conversational Mandarin"
            ]
          }
        ]
      }
    ]
  }
  