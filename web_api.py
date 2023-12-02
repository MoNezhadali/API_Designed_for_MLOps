from flask import Flask, request, jsonify
from model_interface import ModelInterface
import json

app = Flask(__name__)
model_interface = ModelInterface()

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_data = json.loads(input_data)
    prediction = model_interface.predict(input_data)
    # Construct the response JSON here
    response = {
        'request_id': input_data['RequestId'],
        'request_datetime': input_data['RequestDateTime'],
        'merchant_name': input_data['Merchant'],
        'predicted_probability': prediction[0][1],  # Assuming binary classification
        'model_version': model_interface.model_version
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
