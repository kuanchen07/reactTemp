# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/temperature')
def get_temperature():
    # Simulating temperature fetch (replace with actual sensor data if available)
    temperature = round(random.uniform(20, 30), 1)
    return jsonify({"temperature": temperature})

@app.route('/location')
def get_location():
    # List of random locations
    locations = [
        "New York, USA",
        "London, UK",
        "Tokyo, Japan",
        "Sydney, Australia",
        "Paris, France",
        "Berlin, Germany",
        "Moscow, Russia",
        "Rio de Janeiro, Brazil",
        "Cape Town, South Africa",
        "Dubai, UAE"
    ]
    # Randomly choose a location
    location = random.choice(locations)
    return jsonify({"location": location})

if __name__ == '__main__':
    app.run(debug=True)