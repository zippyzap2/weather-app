A React-based web application integrated with a Flask backend to fetch and display real-time weather data for any city. The application provides a user-friendly interface for viewing weather information, including temperature, weather description, and more.

## Features
- **Real-Time Weather Data:** Fetches live weather information from an API based on the user's input.

- **City Search:** Allows users to search for weather details of any city worldwide.

- **Responsive UI:** A modern and interactive user interface optimized for various devices.

- **Error Handling:** Displays user-friendly error messages for invalid inputs or network issues.

## Tech Stack
### Frontend: React.js
- React Components: Modular and reusable components like WeatherForm and WeatherInfo.
- Axios: For making HTTP requests to the backend API.
- CSS: Styled with custom CSS to create an engaging user experience.

### Backend: Flask (Python)
- RESTful API: Provides endpoints for fetching weather data.
- Environment Variables: API keys are securely stored in .env files for safe access.
- Cross-Origin Resource Sharing (CORS): Enabled to allow communication between frontend and backend.

### Weather Data Source
- Powered by the OpenWeatherMap API.

## Installation and Setup
1. Prerequisites
   - Node.js (16.x or 18.x recommended)
   - Python (3.x recommended)
   - npm (comes with Node.js)
   - A free OpenWeatherMap API key
  
2. Clone the Repository
   ```
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```
3. Set Up the Backend
    1. Navigate to the backend/ directory:
         ```
         cd backend
         ```
    2. Create a virtual environment and activate it:
         ```
         python3 -m venv venv
         source venv/bin/activate  # For Windows: venv\Scripts\activate
         ```
     3. Install dependencies:
          ```
          pip install -r requirements.txt
          ```
     4. Create a .env file in the backend/ directory and add your OpenWeatherMap API key:
          ```
          API_KEY=your_openweathermap_api_key
          ```
     5. Start the Flask server:
          ```
          python app.py
          ```
4. Set Up the Frontend
    1. Navigate to the frontend/ directory:
         ```
         cd ../frontend
         ```
    2. Install dependencies:
         ```
         npm install
         ```
     3. Create a .env file in the frontend/ directory and add the backend API URL:
          ```
          REACT_APP_API_BASE_URL=http://localhost:5000
          ```
     4. Start the development server:
          ```
          npm start
          ```
## Usage
1. Open your browser and navigate to http://localhost:3000.
2. Enter the name of a city in the input field and click the "Get Weather" button.
3. View the weather information for the selected city, including temperature and weather description.
4. If no city is entered or there's a network issue, appropriate error messages will be displayed.

## Project Structure

```
weather-app/
├── backend/
│   ├── app.py            # Main Flask application
│   ├── requirements.txt   # Backend dependencies
│   ├── .env               # Environment variables (e.g., API_KEY)
│   └── ...
├── frontend/
│   ├── public/            # Static public files (e.g., index.html)
│   ├── src/               # React source files
│   │   ├── components/    # Reusable React components
│   │   │   ├── WeatherForm.jsx
│   │   │   ├── WeatherInfo.jsx
│   │   │   └── ...
│   │   ├── pages/         # Page-level components
│   │   │   └── HomePage.jsx
│   │   ├── App.jsx        # Main React component
│   │   ├── index.js       # React app entry point
│   │   └── ...
│   ├── .env               # Frontend environment variables
│   └── package.json       # Frontend dependencies and scripts
└── README.md              # Project documentation
```
## Known Issues
- CORS Errors: Ensure the backend has CORS enabled.
- API Limits: The free tier of OpenWeatherMap API has rate limits. Upgrade your plan if necessary.
- City Name Mismatches: Enter valid city names to avoid unexpected errors.

## Future Enhancements
- Geolocation Support: Automatically detect the user's location and display weather.
- Weather Forecasts: Include a 5-day weather forecast.
- Dark Mode: Add a toggle for dark/light themes.
- Multilingual Support: Allow users to view weather data in different languages.

## Contact
- Author: Satish Bezawada
- Email: bsatishaws@gmail.com
- GitHub: https://github.com/zippyzap2
