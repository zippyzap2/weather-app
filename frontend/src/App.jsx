// src/App.jsx
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import homeIcon from './assets/home-icon.png'; // Adjust the path based on your project structure

const App = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);
  const [error, setError] = useState('');

  const fetchWeather = async () => {
    setError('');
    if (!city.trim()) {
      setError('Please enter your location to get weather info.');
      setWeatherData(null);
      return;
    }
    try {
      const response = await axios.get(`http://localhost:5000/weather?city=${city}`);
      setWeatherData(response.data);
    } catch (err) {
      setError('Unable to fetch weather data. Please try again.');
      setWeatherData(null);
    }
  };

  return (
    <>
      <div className="background">
        <div className="sun"></div>
        <div className="cloud cloud1"></div>
        <div className="cloud cloud2"></div>
        <div className="cloud cloud3"></div>
        <div className="cloud cloud4"></div>
      </div>
      <div className="weather-app">
        <h1>Weather App</h1>
        <div className="input-container">
          <input
            type="text"
            placeholder="Enter city name"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
          <button onClick={fetchWeather}>Get Weather</button>
        </div>
        {error && <p style={{ color: 'red', marginTop: '10px' }}>{error}</p>}
        {weatherData && (
          <div className="weather-info">
            <h2>{weatherData.name}</h2>
            <p>Temperature: {weatherData.main.temp} °C</p>
            <p>Weather: {weatherData.weather[0].description}</p>
          </div>
        )}
      </div>
    </>
  );
};

export default App;
