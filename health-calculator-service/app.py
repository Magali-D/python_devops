from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route("/")
def index():
    return "Coucou"

@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()
    try:
        result = calculate_bmi(data["height"], data["weight"])
        if (bmi == 0):
            return jsonify({"error": "Values are incorrect. Height must be in m, weight in kg"}), 400
        return jsonify({"operation": "bmi", "result": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'height' and 'weight'"}), 400

@app.route("/bmr", methods=["POST"])
def subtract_numbers():
    data = request.get_json()
    try:
        result = calculate_bmr(data["height"], data["weight"], data["age"], data["gender"])
        return jsonify({"operation": "bmr", "result": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'height', 'weight', 'age' or 'gender'"}), 400

if __name__ == "__main__":
    app.run(debug=True)