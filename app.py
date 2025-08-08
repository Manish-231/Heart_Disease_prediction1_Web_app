from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model_dt1.pkl')  # Make sure this file is in the same directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form values and convert to floats
        input_features = [
            float(request.form['Age']),
            float(request.form['Sex']),
            float(request.form['ChestPainType']),
            float(request.form['RestingBP']),
            float(request.form['Cholesterol']),
            float(request.form['FastingBS']),
            float(request.form['RestingECG']),
            float(request.form['MaxHR']),
            float(request.form['ExerciseAngina']),
            float(request.form['Oldpeak']),
            float(request.form['ST_Slope']),
            float(request.form['MajorVessels']),
            float(request.form['Thalium'])
        ]

        # Prepare data for prediction
        features = np.array([input_features])
        prediction = model.predict(features)[0]  # Get scalar 0 or 1

        # Render result.html with raw prediction value (0 or 1)
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        # Return error info if something goes wrong
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
