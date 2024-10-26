Sure! Here’s a more concise and polished version of the README for your Flask OTP Verification with Twilio project:

```markdown
# Flask OTP Verification with Twilio

A simple Flask application for user registration and identity verification via One-Time Password (OTP) sent via SMS using Twilio.

## 🌟 Features

- **User Registration**: Sign up with name, email, and phone number.
- **OTP Verification**: Receive OTP via SMS.
- **JWT Authentication**: Secure sessions using JSON Web Tokens.
- **User Data**: Stored in JSON format.

## 🛠️ Requirements

- Python 3.7+
- Flask
- Flask-JWT-Extended
- Twilio
- Standard Libraries: `os`, `time`, `json`

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Set up a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask flask-jwt-extended twilio
   ```

4. **Configure Twilio**: Create a Verify service and get your Twilio credentials.

5. **(Optional) Set environment variables**:
   ```bash
   export JWT_SECRET_KEY='your_jwt_secret_key'
   export TWILIO_ACCOUNT_SID='your_twilio_account_sid'
   export TWILIO_AUTH_TOKEN='your_twilio_auth_token'
   export TWILIO_VERIFY_SERVICE_ID='your_twilio_verify_service_id'
   ```

## 📡 API Endpoints

### Sign Up

**POST /signup**  
Request OTP for a new user.

**Request**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890"
}
```

**Response**: 
- **200 OK**: OTP sent.
- **400 Bad Request**: User already exists or missing fields.

### Login

**POST /login**  
Verify OTP and log in.

**Request**:
```json
{
    "phone": "+1234567890",
    "code": "123456"  // Your OTP
}
```

**Response**:
- **200 OK**: Logged in, returns JWT.
- **401 Unauthorized**: Invalid OTP.
- **404 Not Found**: User not found.

## 🎉 Usage

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Use Postman or curl to interact with the API**.

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

## 📝 License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
