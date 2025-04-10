from flask import Flask, jsonify
from flask_cors import CORS
import requests
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# -------- CONFIGURATION -------- #
API_KEY = "4e9db3f1e6ae8be13a77ca1075e036e1" 
CITY = "Rajkot"
MODEL_PATH = "heatwave_model.pkl"

# -------- FUNCTION: FETCH WEATHER DATA -------- #
def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Rajkot&appid=4e9db3f1e6ae8be13a77ca1075e036e1&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        main = data.get("main", {})
        max_temp = float(main.get('temp_max', 0))
        humidity = float(main.get('humidity', 0))
        pressure = float(main.get('pressure', 0))
        temp = float(main.get('temp', 0))

        if any(val == 0 for val in [max_temp, humidity, pressure, temp]):
            raise ValueError("Some required weather values are missing or zero.")

        return np.array([[max_temp, humidity, pressure, temp]]), {
            "temperature": max_temp,
            "humidity": humidity,
            "pressure": pressure,
            "temp": temp
        }

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None

# -------- FUNCTION: PREDICT HEATWAVE -------- #
def predict_heatwave(features):
    try:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError("Model file not found.")

        model = joblib.load(MODEL_PATH)
        prediction = model.predict(features)
        return int(prediction[0])
    except Exception as e:
        print(f"Prediction error: {e}")
        return None

# -------- API ENDPOINT -------- #
@app.route("/predict", methods=["GET"])
def predict():
    features, weather_info = fetch_weather_data()

    if features is None:
        return jsonify({"error": "Could not fetch weather data"}), 500

    result = predict_heatwave(features)
    if result is None:
        return jsonify({"error": "Prediction failed"}), 500

    is_heatwave = bool(result)
    message = "🔥 Heatwave Alert: Stay hydrated and avoid going out in the afternoon." if is_heatwave else "✅ No heatwave expected. You're good to go!"

    return jsonify({
        "temperature": weather_info["temperature"],
        "humidity": weather_info["humidity"],
        "pressure": weather_info["pressure"],
        "temp": weather_info["temp"],
        "is_heatwave": is_heatwave,
        "message": message
    })

# -------- MAIN -------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
