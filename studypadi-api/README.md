# API Documentation

## Account Authentication
Implemented 2FA for user creation. an email is sent to the registered email address. Upon login, a JWT access and refresh token is returned. This token should to used to access restricted endpoints

### Endpoints
- /test GET
- /api/v1/signup/ POST
- /api/v1/verify-otp/ POST
- /api/v1/resend-otp/ POST
- /api/v1/login POST
- /api/vi/dashboard GET
- /api/vi/forget-password POST
- /api/vi/reset POST

### Description
- Test: a get request to test if the application is receiving request

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
  
- Dashboard: This is a test endpoint to get a dummy resources that requires authentication. Include an header called Authorisation with a value of "Bearer {access token}"
  ##### E.g
  ###### Output
  ```
  {
      "msg":"working"
  }
  ```

- Forget-password: Endpoint to initiate a forget password. The base url is the url of the frontend application that calls it. This will be used to generate a reset link that would be sent to the email of the user. Clicking on the link should direct the user to a page in the front end application to reset teir password.
  ##### E.g
  ###### Input
  ```
  {
      "email": "abc1@email.com",
      "base_url": "http://127.0.0.1:8000"
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
