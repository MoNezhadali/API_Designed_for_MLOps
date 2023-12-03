# Built-in python libraries
import logging
# Side-packages
from flask import Flask, request, jsonify
# internal imports
from model_interface import ModelInterface
from utilities import check_input_necessities

# internal imports

# Configure logging
logging.basicConfig(filename='application.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Take the flask instance
app = Flask(__name__)

# Take the ml model instance
model_interface = ModelInterface()

def generate_response(data, model_prediction):
    response = {
        'request_id': data['RequestId'],
        'request_datetime': data['RequestDateTime'],
        'merchant_name': data['Merchant'],
        'predicted_probability': model_prediction[0][1],
        'model_version': model_interface.model_version
    }
    return response


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data
        input_data = request.json
        # Checking if all the inputs are sent
        check_input_necessities(input_data)
        # Predict using the ml model
        prediction = model_interface.predict(input_data)
        # Construct the response JSON
        response = generate_response(input_data, prediction)
        # return response
        return jsonify(response)
    
    except ValueError as e:
        logging.error(f"Value error: {e}")
        return jsonify({'error': str(e), 'status': 400}), 400
    except Exception as e:
        logging.error(f"Error in prediction: {e}")
        return jsonify({'error': 'Internal server error', 'status': 500}), 500

if __name__ == '__main__':
    app.run(debug=True)
