from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained Random Forest model
model_path = 'model/random_forest_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index2.html')  # Render HTML file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from form data
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Combine inputs into a 2D list for model prediction
        inputs = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]

        # Perform prediction using the model
        predicted_crop = model.predict(inputs)[0]

        # Return prediction as JSON
        return jsonify({"recommendation": predicted_crop})
    except Exception as e:
        # Handle any errors that occur during prediction
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
