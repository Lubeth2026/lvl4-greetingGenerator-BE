
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello from the Greeting Generator backend!"

@app.route("/greetings", methods=["POST"])
def greeting():
    data = request.json
    name = data["name"]

    with open("greeting.json") as file:
        greetings_data = json.load(file)

    greeting_template = random.choice(greetings_data['greetings'])
    message = greeting_template.replace( "{name}", name )

    return jsonify({"message": message})
