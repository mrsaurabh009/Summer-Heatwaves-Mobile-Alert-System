# 🔥 Summer Heatwave Alert System

A real-time mobile + AI-based alert system that predicts extreme heatwaves and notifies users instantly via an Android app, using live weather data and a machine learning model.

## 📱 Project Overview

**Summer Heatwave Alert System** is designed to enhance public safety during rising climate challenges. The system leverages:
- ✅ Historical climate analysis
- ✅ AI/ML prediction (Random Forest Classifier)
- ✅ Live weather data from OpenWeatherMap API
- ✅ Flask API for predictions
- ✅ Flutter-based cross-platform mobile app
- ✅ Render deployment for live model hosting

---

## 🌟 Features

- 🌡️ **Live Weather Monitoring**
- 🔮 **AI-Powered Heatwave Prediction**
- 📲 **Mobile App for Real-Time Alerts**
- 🔔 **User Alerts with Severity Message**
- ☁️ **Cloud-hosted API (Render)**
- 🧠 **Machine Learning (Python + scikit-learn)**

---

## 🛠️ Tech Stack

| Layer            | Technologies                                  |
|------------------|-----------------------------------------------|
| AI/ML            | Python, Pandas, scikit-learn, joblib           |
| Weather API      | OpenWeatherMap API                            |
| Backend API      | Flask, Flask-CORS, Requests                    |
| Mobile App       | Flutter, Dart, HTTP Client                     |
| Deployment       | Render (for Flask)                            |
| Model Deployment | `.pkl` file hosted and served live            |

---

## 🚀 How It Works

1. **Historical Data Analysis**  
   Trained on weather data to detect patterns where `MaxTemp > 35°C` for 3+ consecutive days.

2. **Model Training**  
   Using Random Forest Classifier with features like:
   - MaxTemp
   - Temp3pm
   - Humidity3pm
   - Pressure3pm

3. **Live Integration**  
   Flask server fetches live weather data via OpenWeatherMap API, processes it, and makes predictions.

4. **Mobile App**  
   Flutter app displays weather and heatwave alerts using data from the deployed Flask API.



## ⚙️ Setup Instructions

### 🔌 Flask API

1. Clone the repo
2. Install dependencies:

pip install -r requirements.txt

deploy to Render with start command: python app.py 


🎯 Success Metrics
🔁 Accuracy: > 90% on labeled historical heatwaves

⚡ Response time: < 1s for prediction

📲 Alert delivery: Real-time updates on mobile
