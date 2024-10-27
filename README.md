# Webstack - Portfolio Project

## Project Introduction: StudyPadi – Your Personalized Study Partner

StudyPadi is a unique quiz-based study platform designed to enhance the learning experience for students across various fields of study. Unlike traditional quiz apps, StudyPadi acts as both a learning assistant and a study companion, offering an interactive and personalized revision experience. The platform aims to support users by not only serving pre-existing questions but also generating new questions based on user-submitted study materials.

StudyPadi enhances comprehension through active learning and self-testing, turning study sessions into a dynamic and engaging process. It offers features like:
- **Past Question Banks:** Curates questions from various fields, starting with radiology.
- **Automated Question Generation:** Leverages AI to create questions from user-provided study content.
- **Collaborative Learning:** Allows users to create and share quizzes with others, forming study groups.
- **Scalability:** Supports the creation of new domains and subdomains as the platform grows, adaptable to various fields of study.
- **And many more**

StudyPadi is more than a quiz app; it’s a learning ecosystem designed to help users prepare for exams and assessments by providing a customized and interactive learning experience.

## Project

### Technlogies and packages used
- MySQL database
- Redis cache and message broker
- Celery: Asynchronous task queue. Used to handle sending OTP to email using redis as the broker
- pyotp: For generating Time based OTP
- django rest framework
- django rest framework simple jwt

## API Documentation

### Account Authentication
Implemented 2FA for user creation. an email is sent to the registered email address. Upon login, a JWT access and refresh token is returned. This token should to used to access restricted endpoints

#### Endpoints
- /api/v1/signup/ POST
- /api/v1/verify-otp/ POST
- /api/v1/resend-otp/ POST
- /api/v1/login POST

#### Description
- Signup: receives the following required fields and returns a user object and a message indicating that an otp has been sent:
  * email
  * first_name
  * last_name
  * password
  * confirm_password 

- Verify-otp: receives the follwoing required fields and returns json of email and message
  * otp
  * email

- Resend-otp: receives an email field and returns json of email and message

- Login: receives the email and password fields and returns  the following fields
  * email
  * first_name
  * last_name
  * access_token
  * refresh_token
