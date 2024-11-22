# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'message': 'City parameter is required.'}), 400

    try:
        # Make a request to the OpenWeatherMap API
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
        response = requests.get(weather_url)
        data = response.json()

        if data.get('cod') != 200:
            return jsonify({'message': data.get('message', 'Error fetching weather data.')}), data.get('cod', 500)

        # Extract relevant data
        weather_data = {
            'name': data['name'],
            'main': {
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure']
            },
            'weather': data['weather'],
            'wind': data['wind'],
            'sys': data['sys']
        }

        return jsonify(weather_data), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred while fetching weather data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
