import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle
import ngrok

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@flask_app.route('/')
def Home():
    return render_template('index.html')

@flask_app.route('/submit', methods = ['POST'])
def submit():
    try:
        input_data = [float(x) for x in request.form.values()]
        input_array = np.array(input_data).reshape(1,-1)
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)

        result = "diabetic" if prediction[0] == 1 else "not diabetic"
        return render_template('index.html', prediction_text=f"The person is {result}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)