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
- setup mysql
  ```
  $ docker volume create mysql-volume
  $ docker run --name mysql-db -e MYSQL_ROOT_PASSWORD='Mys&l_D3' -p 3307:3306 -v mysql-volume:/var/lib/mysql -d mysql
  ```
- Rename the .environ.test file to .environ, and update the EMAIL_USER and EMAIL_APP_PASSWORD variable to your gmail value. Research on how to get it. This will enable OTP to be sent when registering users.
- start the application: You can use gunicorn web server or django builtin server:
  `gunicorn studypadi.wsgi:application --bind 0.0.0.0:8000`
  OR
  `python3 manage.py runserver`
- Run celery worker service. This handles email sending asynchronously
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
#### GET and POST request
- api/v1/modules/?size=<> page=<> GET/POST
- api/v1/submodule/?module=<> | size=<> page=<> GET/POST
- api/v1/section/?submodule=<> | size=<> page=<> GET/POST
- api/v1/topic/?section=<> | size=<> page=<> GET/POST
#### GET requests
- api/v1/user/ GET
- api/v1/user/quiz/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/prefilled/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/realtime/?quizid=<> | size=<> page=<> GET
- api/v1/user/quiz/revision-test/?quizid=<> | size=<> page=<> GET
- api/v1/quiz/?module=<> | submodule=<> | section=<> | topic=<>  | educator_id=<>  | educator_name=<> | quizid=<> | quiz_name=<> | size=<> page=<> GET
- api/v1/quiz/question/quizid=<> GET
#### POST requeests
- api/v1/question/create POST

**NOT IMPLEMENTED**
- api/v1/user/quiz/response/?id
- api/v1/question/?id=<>
- api/v1/quiz/generate/ POST
- api/v1/quiz/save/ POST
- api/v1/quiz/submit/ POST
- api/v1/quiz/create/ POST
- api/v1/submit-material POST

### Description
- modules/ :endpoint to get all modules, or create modules using a list of module objects
- submodules/  
- sections/    
- topics/  
- user/  
- user/quiz/ 
- user/quiz/prefilled/    
- user/quiz/realtime/ 
- user/quiz/revision-test/
- quiz/  
- quiz/question/   
- quiz/generate/   
- quiz/save/ 
- quiz/submit/ 
- quiz/create/ 
- question/  
- question/create/ 
- submit-material/ 