from flask import Flask, request, jsonify
import pickle
import numpy as np
import traceback

app = Flask(__name__)

# Load the trained model
try:
    with open("heatwave_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("❌ Error loading model:", e)
    model = None


@app.route('/')
def home():
    return "🔥 Heatwave Prediction API is running!"


@app.route('/predict', methods=["POST"])
def predict():
    try:
        data = request.get_json()
        # Change these fields to match the actual inputs your model expects
        input_data = np.array([[
            data['temperature'],
            data['humidity'],
            data['wind_speed']
        ]])

        prediction = model.predict(input_data)
        return jsonify({"heatwave": bool(prediction[0])})

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 400


if __name__ == '__main__':
    app.run(debug=True)
