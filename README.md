# Flask OTP Verification with Twilio

This is a simple Flask application that allows users to sign up using their phone numbers and verify their identity through a One-Time Password (OTP) sent via SMS. It uses Twilio's Verify API for OTP management and Flask-JWT-Extended for user authentication.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
  - [Sign Up](#sign-up)
  - [Login](#login)
- [Usage](#usage)
- [License](#license)

## Features

- User registration with name, email, and phone number.
- OTP verification via SMS using Twilio.
- JWT-based authentication after successful verification.
- User data stored in JSON format.

## Requirements

- Python 3.7 or higher
- Flask
- Flask-JWT-Extended
- Twilio
- `os`, `time`, `json` (standard libraries)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install Flask flask-jwt-extended twilio
   ```

4. Set up your Twilio account and create a Verify service. Obtain your Twilio Account SID, Auth Token, and Verify Service SID.

5. (Optional) Set your environment variables:
   ```bash
   export JWT_SECRET_KEY='your_jwt_secret_key'
   export TWILIO_ACCOUNT_SID='your_twilio_account_sid'
   export TWILIO_AUTH_TOKEN='your_twilio_auth_token'
   export TWILIO_VERIFY_SERVICE_ID='your_twilio_verify_service_id'
   ```

## Configuration

The main configuration parameters are defined in the code:
- **JWT_SECRET_KEY**: Secret key for JWT. Change this in production.
- **Twilio Configuration**: Set your Twilio credentials directly in the code or via environment variables.

## API Endpoints

### Sign Up

**POST /signup**

This endpoint allows a new user to sign up and request an OTP.

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890"
}
```

**Response**:
- 200 OK: OTP sent to your phone.
- 400 Bad Request: Missing fields or user already exists.

### Login

**POST /login**

This endpoint verifies the OTP and logs the user in.

**Request Body**:
```json
{
    "phone": "+1234567890",
    "code": "123456"  // Replace with the actual OTP
}
```

**Response**:
- 200 OK: Verification successful, returns JWT access token.
- 401 Unauthorized: Invalid or expired OTP.
- 404 Not Found: User not found.

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Use tools like [Postman](https://www.postman.com/) or `curl` to interact with the API.

### Example curl commands:

- **Sign Up**:
   ```bash
   curl -X POST http://127.0.0.1:5000/signup \
   -H "Content-Type: application/json" \
   -d '{ "name": "John Doe", "email": "john.doe@example.com", "phone": "+1234567890" }'
   ```

- **Login**:
   ```bash
   curl -X POST http://127.0.0.1:5000/login \
   -H "Content-Type: application/json" \
   -d '{ "phone": "+1234567890", "code": "123456" }'
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
#   p y t h o n _ a p i _ O T P  
 #   o t p _ a p i _ p y t h o n  
 #   o t p _ a p i _ p y t h o n  
 #   o t p _ a p i _ p y t h o n  
 #   o t p _ a p i _ p y t h o n  
 