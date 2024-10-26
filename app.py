from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from twilio.rest import Client
import os
import time
import json

app = Flask(__name__)

# Configuration
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key")  # Change this in production
jwt = JWTManager(app)

# Twilio Configuration from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Your Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")      # Your Twilio Auth Token
TWILIO_VERIFY_SERVICE_ID = os.getenv("TWILIO_VERIFY_SERVICE_ID")  # Your Verify Service SID

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Path to the JSON file for storing user data
USERS_FILE = 'users.json'

# Function to load users from JSON file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Function to save users to JSON file
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Load existing users at startup
users = load_users()

# Route to sign up (request OTP)
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email or not phone:
        return jsonify({"message": "Name, email, and phone number are required"}), 400

    # Check if user already exists
    if phone in users:
        return jsonify({"message": "User already exists, please log in"}), 400

    # Send OTP via Twilio Verification API
    try:
        verification = client.verify \
            .v2 \
            .services(TWILIO_VERIFY_SERVICE_ID) \
            .verifications \
            .create(to=phone, channel='sms')

        # Save user information temporarily until OTP is verified
        users[phone] = {
            "name": name,
            "email": email,
            "phone": phone,
            "created_at": time.time(),
            "is_verified": False  # Initially, the user is not verified
        }

        # Save the updated users to the JSON file
        save_users(users)

        return jsonify({"message": "OTP sent to your phone"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to send OTP", "error": str(e)}), 500


# Route to verify OTP and register/login
@app.route("/login", methods=["POST"])
def verify_otp():
    data = request.get_json()
    phone = data.get("phone")
    code = data.get("code")

    if not phone or not code:
        return jsonify({"message": "Phone number and OTP are required"}), 400

    # Verify the OTP using Twilio Verify API
    try:
        verification_check = client.verify \
            .v2 \
            .services(TWILIO_VERIFY_SERVICE_ID) \
            .verification_checks \
            .create(to=phone, code=code)

        if verification_check.status == 'approved':
            # Register the user if not already registered
            if phone in users:
                users[phone]["is_verified"] = True  # Mark user as verified
                name = users[phone]["name"]
                email = users[phone]["email"]

                # Save the updated users to the JSON file
                save_users(users)

                # Generate a JWT token with user information
                access_token = create_access_token(identity={"phone": phone, "name": name, "email": email})

                return jsonify({"message": "Verification successful, you are logged in.", "access_token": access_token}), 200
            else:
                return jsonify({"message": "User not found, please signup first"}), 404
        else:
            return jsonify({"message": "Invalid or expired OTP"}), 401
    except Exception as e:
        return jsonify({"message": "Failed to verify OTP", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0' , port=5000)
