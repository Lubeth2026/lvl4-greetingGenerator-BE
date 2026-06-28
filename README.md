# Greeting Generator - Backend

## Overview
The Greeting Generator backend is a Flask API that receives a user's name and returns a personalized greeting.
The backend is responsible for:
- Receiving HTTP requests
- Reading JSON data from requests
- Loading greeting templates from a JSON file
- Creating personalized messages
- Returning JSON responses to the frontend

### How It Works
The frontend sends a POST request containing a user's name.
The Flask API:
1. Receives the request.
2. Extracts the name.
3. Opens the greetings.json file.
4. Selects a random greeting.
5. Replaces `{name}` with the user's name.
6. Sends the response back.

# API Endpoint
/POST
http://localhost:5000/greetings

#### Running The Backend
1. Clone the repository
2. Navigate into the project:
3. Create a virtual environment
python -m venv .venv
source .venv/Scripts/activate
4. Install dependencies
pip install flask
pip flask-cors
pip freeze > requiremtns.txt
5. Start Flask server
flask run
6. The API will run at:
http://127.0.0.1:5000
