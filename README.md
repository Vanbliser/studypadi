# Webstack - Portfolio Project

## 📚 Project Introduction: StudyPadi – Your Personalized Study Partner

**StudyPadi** is a unique quiz-based study platform designed to transform the learning experience for students across various fields of study. Unlike traditional quiz apps, StudyPadi serves as both a learning assistant and a study companion, providing both the features of a Traditional Quiz App and a personalized revision experience. The platform leverages advanced AI algorithms to generate tailored questions, making it ideal for self-study and group learning sessions.

StudyPadi enhances comprehension through active learning and self-testing, turning study sessions into dynamic, engaging, and effective processes. The platform is scalable and adaptable, supporting users from various academic backgrounds and domains.

### Key Features
- **🌍 Past Question Banks**: Curates questions from various fields and domains which have been well classified into different categories, for better and easier access the user.
- **🧠 AI-Assisted Question Generation**: Uses artificial intelligence to generate questions from user-submitted study materials, creating a personalized learning experience.
- **👥 Collaborative Learning**: Users with the "Educator" User Roles can create, share, and collaborate on quizzes, Enriching the Questions Bank that providing Quizes with real Significance by Proffesionals in that sector.
- **🔄 Modular Learning Structure**: Supports classification of educational content into domains, submodules, sections, and topics for targeted learning.
- **🎯 Quiz Generation Algorithms**: Offers multiple quiz generation algorithms, including random, adaptive, and user-focused quiz modes.
- **📊 Dashboard & Analytics**: Provides users with a comprehensive dashboard to track quiz performance, study history, and progress over time.
- **⚙️ Scalability**: The platform is designed to scale, allowing the addition of new study domains, subdomains, and categories as the user base grows.

## Project Description

### Technlogies and packages used

### Backend
- **MySQL database**
- **Redis cache and message broker**
- **Celery**: Asynchronous task queue. Used to handle sending OTP to email using redis as the broker
- **pyotp**: For generating Time based OTP
- **django rest framework**
- **django rest framework simple jwt**
- **gunicorn**: Application server
- **Open-AI API**


---

### Frontend
- **HTML5 & CSS3**: For creating the structure and styling of the web pages.
- **JavaScript (ES6+)**: Provides dynamic functionality and interactivity.
- **React**: Powers the component-based architecture of the platform.
- **Next.js**: Used for server-side rendering, improving performance and SEO.
- **Uizard AutoDesign**: Leveraged for AI-powered UI mockups to accelerate the design process, and provide aframework towork on other designs.
- **Figma**: For bringing Design ideas into life, and testing decisions before final implementation.
- **Miro**: For Whiteboarding and collaborative sessions.


---

## 🗂️ Pages Available on the Frontend

### 1. **Landing Page**
- **URL**: `/`
- **Description**: Welcomes users with a captivating hero section, a quick overview of features, and easy navigation to registration or login pages.
- **Key Components**:
  - Header with Call-to-Action (CTA) buttons (Register, Login)
  - Feature highlights showcasing the benefits of using StudyPadi
  

### 2. **Authentication**
- **Sign Up**: 
  - **URL**: `/auth/register`
  - **Description**: New users can create an account using email registration. after which an OTP with a link is sent to their email, so they can authorize thier account
- **Login**:
  - **URL**: `/auth/login`
  - **Description**: Existing users can access their accounts using secure login.

  - **User Roles**: There are Three User Roles Available which is the Student (base user), Educator and Admin. on SignUp every account is a base user untill this privileges are upgraded from the backend.

### 3. **Dashboard**
- **URL**: `/dashboard`
- **Description**: Centralized dashboard providing an overview of the user's quiz history, performance analytics, and study progress.
- **Key Components**:
  - Progress tracker for completed quizzes
  - Graphical representation of quiz scores and performance trends
  - Quick links to start new quizzes or access study materials

### 4. **Quiz Bank**
- **URL**: `/quizzes`
- **Description**: A categorized list of quizzes available, including past questions from various fields.
- **Key Features**:
  - Filter options by domain, module, and difficulty level
  - Access to community-shared quizzes
  - Access to AI generated tests from Different Users Material

### 5. **Quiz Interface**
- **URL**: `/quiz/[quizID]`
- **Description**: Interactive quiz-taking page where users answer questions in a timed environment.
- **Key Features**:
  - Supports multiple question types (MCQs, True/False, etc.)
  - Provides instant feedback on answers
  - Adaptive quiz modes based on user performance

### 6. **Revision Test**
- **URL**: `/test`
- **Description**: Users can upload and manage study materials, which are analyzed by AI to generate custom quizzes.
- **Key Components**:
  - AI-assisted study material analysis
  - Upload options for documents and notes
  - Study material categorization by modules and topics

### 7. **Profile Management**
- **URL**: `/profile`
- **Description**: Manage user profile details, preferences, and notification settings.
- **Key Features**:
  - Update profile information
  - Manage study preferences and quiz notifications

---

## 📚 API Documentation

The API documentation is available in the [studypadi_api] https://github.com/Vanbliser/studypadi/blob/main/studypadi-api/README.md folder. It covers the following endpoints:
- **User Authentication**: Register, login, and manage user sessions.
- **Quiz Management**: CRUD operations for quizzes, including fetching, creating, and deleting quizzes.
- **Study Material Upload**: Endpoints for analyzing and storing user-uploaded documents.
- **Dashboard**: Track user quiz history and generate performance reports.

---

## 🛠️ How to Set Up Locally

### Setting Up Frontend

### Prerequisites
- **Node.js** (v12.22.12 or above)
- **npm** (v6.14.16 or above)
- **Python 3.8+**

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vanbliser/studypadi.git
   cd studypadi_FE/studypadi
   npm install
   npm run dev
   
### Setting Up Backend
- **Django** (v5.1.2 or above)
- **redis** (v5.2.0 or above)
- **Python 3.8+**
- **Docker**
other requirements are in the requirement.txt file.

## 🛠️ Setting Up MySQL

1. **Create a Docker Volume for MySQL**
   ```bash
   docker volume create mysql-volume
2. Run MySQL Docker Container
    ```bash
docker run --name mysql-db \
  -e MYSQL_ROOT_PASSWORD='Mys&l_D3' \
  -p 3307:3306 \
  -v mysql-volume:/var/lib/mysql \
  -d mysql
## 🛠️ Setting Up MySQL
### Create a Docker Volume for Redis

    ```bash
    docker volume create redis-volume
    cd studypadi-api
    docker run --name redis \
    -p 6379:6379 \
    -v redis-volume:/data \
    -v $(pwd)/redis.conf:/usr/local/etc/redis/redis.conf \
    -d redis redis-server

##  🛠️ Setting Up Django
### Create a Virtual Environment

bash
Copy code
cd studypadi-api
python3 -m venv .env
source .env/bin/activate
Install Python Dependencies

bash
Copy code
pip3 install -r requirements.txt
Apply Database Migrations

bash
Copy code
python manage.py migrate
Run the Django Server using Gunicorn

Open a new terminal and execute:
bash
Copy code
gunicorn studypadi.wsgi:application --bind 127.0.0.1:8000
🧪 Testing Your Setup
To confirm everything is set up correctly, visit the following URL in your browser:

URL: http://127.0.0.1:8000/api/v1/test
