# Studypadi API Project Setup

- clone the project
- cd into studypadi-api
  `cd studypadi-api`
- create a python virtual environment:
  `python3 -m venv .env`
- activate virtual environment: 
  `source .env/bin/activate`
- install dependencies: 
  `pip3 install -r requirements.txt`
- download and setup redis. Make sure you have docker
  ```
  $ docker volume create redis-volume
  $ docker run --name redis -p 6379:6379 -v redis-volume:/data -v $(pwd)/redis.conf:/usr/local/etc/redis/redis.conf -d redis redis-server
  ```
  Going forward, like when you restart your laptop, you just need to run `docker container start redis`
- setup mysql
  ```
  $ docker volume create mysql-volume
  $ docker run --name mysql-db -e MYSQL_ROOT_PASSWORD='Mys&l_D3' -p 3307:3306 -v mysql-volume:/var/lib/mysql -d mysql
  ```
  Going forward, like when you restart your laptop, you just need to run `docker container start mysql-db`
- Rename the .environ.test file to .environ, and update the EMAIL_USER and EMAIL_APP_PASSWORD variable to your gmail value. Research on how to get it. This will enable OTP to be sent when registering users. Also add your openai key with access to gpt-4o-mini model.
- make database migrations `python3 manage.py makemigrations`
- migrate database `python3 manage.py migrate`
- start the application: You can use gunicorn web server or django builtin server:
  `gunicorn studypadi.wsgi:application --bind 0.0.0.0:8000`
  OR
  `python3 manage.py runserver`
- Run celery worker service in another terminal window. This handles email sending asynchronously
  `python -m celery -A studypadi worker -l info`


# API Documentation

## Test

### Endpoints
- /test GET

### Description
- Test: a get request to test if the application is live

## Account Authentication
Implemented 2FA for user creation. an email is sent to the registered email address. Upon login, a JWT access and refresh token is returned. This token should to used to access restricted endpoints

### Endpoints
- /api/v1/auth/signup/ POST
- /api/v1/auth/verify-otp/ POST
- /api/v1/auth/resend-otp/ POST
- /api/v1/auth/login POST
- /api/vi/auth/forget-password POST
- /api/vi/auth/reset POST
- /api/vi/auth/logout POST
- /api/vi/auth/refresh-token POST
- /api/vi/auth/test-auth GET

### Description
- Signup: receives the following required fields and returns a user object and a message indicating that an otp has been sent:
  * email
  * first_name
  * last_name
  * password
  * confirm_password 
  ##### E.g
  ###### Input
  ```
  {
    "email": "abc1@email.com",
    "first_name": "Abc",
    "last_name": "Xyz",
    "password": "Password123",
    "confirm_password": "Password123"
  }
  ```
  ###### Output
  ```
  {
    "user": {
  "email":"abc1@email.com",
  "first_name":"Abc",
  "last_name":"Xyz"
  },
    "message": "An OTP has been sent to the registered email"
  }
  ```

- Verify-otp: receives the follwoing required fields and returns json of email and message
  * otp
  * email
  ##### E.g
  ###### Input
  ```
  {
    "otp": 234566,
    "email": "abc1@email.com"
  }
  ```
  ###### Output
  ```
  {
    "message": "User already verified",
    "email": "abc1@email.com"
  }
  ```

- Resend-otp: receives an email field and returns json of email and message
  ##### E.g
  ###### Input
  ```
  {
    "email": "abc1@email.com"
  }
  ```
  ###### Output
  ```
  {
    "message": "User already verified",
    "email": "abc1@email.com"
  }
  ```

- Login: receives the email and password fields and returns the following fields
  * email
  * first_name
  * last_name
  * access_token
  * refresh_token
  ##### E.g
  ###### Input
  ```
  {
    "password": "123456",
    "email": "abc1@email.com"
  }
  ```
  ###### Output
  ```
  {
    "email":"abc1@email.com",
    "first_name":"Abc",
    "last_name":"Xyz",
    "access_token": "<access token>",
    "refresh_token": "<refresh token>"
  }
  ```

- Forget-password: Endpoint to initiate a forget password. The base url is the url of the frontend application that calls it. This will be used to generate a reset link that would be sent to the email of the user. Clicking on the link should direct the user to a page in the front end application to reset teir password. The reset link will be made up of the base url and query strings represeniting the user id and a token url encoded. e.g "http://127.0.0.1:8000/set-new-password?user_id=OA&token=cfugxn-cd0fee5261e44cd75201cdf303e53af1"
  ##### E.g
  ###### Input
  ```
  {
    "email": "abc1@email.com",
    "base_url": "http://127.0.0.1:8000/set-new-password"
  }
  ```
  ###### Output
  ```
  {
    "message": "A link has been sent to your email to reset your password"
  }
  ```

- Reset: Endpoint to reset password. This endpoint wuld be used after a user clicks on the reset link. Valuable information will be gotten from the link and used to formulate this POST request
  ##### E.g
  ###### Input
  ```
  {
    "uidBase64": "OA",
    "token": "cflxfv-8330b54f6bb9586800374645275ec45c",
    "new_password": "123456",
    "confirm_password": "123456"
  }
  ```
  ###### Output
  ```
  {
    "message": "Password changed succesfully"
  }
  ```

- Logout: An endpoint to logout, effectively blacklisting the current refresh token. Returns a 205 resent content or 400 bad request.
  ##### E.g
  ###### Input
  ```
  {
    "refresh_token": "<refresh token>"
  }
  ```

- Refresh-token: An endpoint to get a access token using a refresh token
  ##### E.g
  ###### Input
  ```
  {
    "refresh": "<refresh token>"
  }
  ```
  ###### Output
  ```
  {
    "access": "<new access token>",
    "refresh": "<new refresh token>
  }
  ```
  
- Test-auth: This is a test endpoint to get a dummy resources that requires authentication. Include an header called Authorisation with a value of "Bearer {access token}"
  ##### E.g
  ###### Http header
  ```
  Authorization Bearer "<access token>"
  ```
  ###### Output
  ```
  {
    "msg":"working"
  }
  ```

## main

### Endpoints
Note that a postman collection has been addesd to this repo

#### GET POST and PATCH request
- api/v1/modules/?id=<> | size=<> page=<> GET/POST/PATCH
- api/v1/submodule/?module_id=<> | size=<> page=<> GET/POST/PATCH
- api/v1/section/?submodule_id=<> | size=<> page=<> GET/POST/PATCH
- api/v1/topic/?section_id=<> | size=<> page=<> GET/POST/PATCH
#### GET requests
- api/v1/user/ GET
- api/v1/user/quiz/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/prefilled/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/realtime/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/revision-test/?quizid=<> | size=<> page=<> GET
- api/v1/quiz/?moduleid=<> | submoduleid=<> | sectionid=<> | topicid=<>  | educatorid=<>  | educator_name=<> | quizid=<> | quizname=<> search=<> | size=<> page=<> GET
- api/v1/quiz/question/quizid=<> GET
- api/v1/question/?id=<> GET
- api/v1/user/quiz/response/?quizid GET
#### POST requeests
- api/v1/question/create POST
- api/v1/quiz/generate/ POST
- api/v1/submit-material POST
- api/v1/quiz/save/ POST
- api/v1/quiz/submit/ POST
- api/v1/quiz/create/ POST

### Description
- modules/ :endpoint to get all modules, or create/update modules using a list of module objects with the following parameter:
  - id (int, optional-include if you want to update an existing module)
  - title (string)
  - description (string)
- submodules/  :same as above with an additional module_id required parameter. submodules must belong to a module.
  - id (int, optional-include if you want to update an existing submodule)
  - module_id (int)
  - title (string)
  - description (string)
- sections/  :same as above with a required submodule_id parameter
- topics/  :same as above with a required submodule_id parameter
- user/  :returns an object representing the current authenticated user.
- user/quiz/ :returns a list of all quizzes taken by the current user, or a single quiz if you provide a quizid value
- user/quiz/prefilled/  :same as above just prefilled quiz 
- user/quiz/realtime/  :same as above, just realtime quiz
- user/quiz/revision-test/ :same as above, just revision-test quiz
- user/quiz/response/ id=<> : returns a taken quiz or all quizzes of a user, with all questions, options, and choses option of the user
- quiz/  :returns a list of quizzes following the support query strings. precedence is as follows quizid > educatorid > topicid > sectionid > submoduleid > moduleid > quizname == educatorname == search
- quiz/question/  :returns all questions associated with a quiz provided by the quizid parameter
- quiz/generate/ :generate quiz by applying the following filter (module, submodule, section, topic, question_type, difficulty, algorithm), where:
  - QUESTION_TYPE
      - AIG: AI Generated quiz
      - EDQ: Educator quiz
      - PAQ: Past question quiz
      - AIE: AI Generated and Educator quiz
      - AIP: AI Generated and Past question quiz
      - ALL: All type
  - DIFFICULTY
      - EAS - Easy
      - MED - Medium
      - HRD - Hard
      - EAM - Easy AND Medium
      - EAH - Easy AND Hard
      - EMD - Easy AND Medium AND Hard
  - ALGORITHM
      - RAD - Random
      - MOF - Most failed
      - LEA - Least attempted
- submit-material/ :receives a JSON with name, num_of_questions, and text fields. The name represent the name of the quiz that would be generated. num_of-questions represent the num of question you want generated, and text represent the study material text that questions would be generated out of.
- question/ :get all questions or a single question if you provide the id of the question in a query parameter 'id'
- question/create/ :takes in a list of questions each with all their associated options. 
- quiz/save/ :takes the following: and returns same with populated ids
```
{
  "quiz_attempt_id": 18,
	"quiz_id": 1,
	"responses":
	[
		{
      "question_id": 2,
      "chosen_option": 7
		},
		{
      "question_id": 1,
      "chosen_option": 2
		}
	]
}
```
- quiz/submit/ :same as above but changes the status to FIN. Submitted quiz cannot be edited and saved
- quiz/create/ :for creating quiz. Takes the following and returns same with popuated IDs
```
{
    "name": "new quiz",
    "questions": [
        {
            "question": "What is the name of the Developer of this App",
            "difficulty": "EAS",
            "options": [
                {
                    "option": "Blossom",
                    "is_answer": true
                },
                {
                    "option": "David",
                    "is_answer": false
                },
                {
                    "option": "Joe",
                    "is_answer": false
                },
                {
                    "option": "Jane",
                    "is_answer": false
                }
            ]
        },
        {
            "question": "What is the Diameter of the Earth",
            "difficulty": "EAS",
            "options": [
                {
                    "option": "10000km",
                    "is_answer": true
                },
                {
                    "option": "12000",
                    "is_answer": false
                },
                {
                    "option": "13000",
                    "is_answer": false
                },
                {
                    "option": "3600km",
                    "is_answer": true
                }
            ]
        }
    ]
}
```
