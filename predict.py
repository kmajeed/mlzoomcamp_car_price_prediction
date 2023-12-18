# library imports
import pandas as pd
import numpy as np
import joblib
from flask import Flask, request, jsonify

# Disabling warnings:
import warnings
warnings.filterwarnings('ignore') 


def predict_single(car, preprocessor, model):   
    # trnsform car data using OneHotEncoder and PowerTransformer
    X = preprocessor.transform(car)
    # make prediction
    y_pred = model.predict(X)
    
    return y_pred
# previously saved model
model = joblib.load('model.joblib')
#pre processor 
preprocessor = joblib.load('preprocessor.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # read json data
    data_in = request.get_json()
    # convert into data frame
    car = pd.DataFrame([data_in])     
    # get predicted price
    prediction = predict_single(car, preprocessor, model)
    
    result = { 'predicted price ': float(prediction[0])
    }
    #print(result)
    #return 'You can sell your call for £{0}'.format(float(prediction[0]))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)