from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with your actual API key
API_KEY = "17245e4b9f8397d4509abbccd8e82a59"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not provided"}), 400

    # Call the OpenWeatherMap API (example)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        return jsonify({"error": "City not found"}), 404

    if response.status_code != 200:
        return jsonify({"error": "Unable to fetch weather data"}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)