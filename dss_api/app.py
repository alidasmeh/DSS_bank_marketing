from flask import Flask, request, jsonify
from flask_cors import CORS

import joblib
import pandas as pd
import sklearn

from categories_to_number import categories_to_number
from fill_missing_values import fill_missing_values

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()

    new_predict = pd.DataFrame([data])

    result = fill_missing_values(new_predict)

    if result['status'] == False: 
        return jsonify({"message": "process failed", "error": "there are missing values that cannot be fill automatically."})

    else:
        new_predict_converted = categories_to_number(result['dataframe'])

        loaded_model = joblib.load(app.root_path+"/static/dss_bank_marketing_trained_model.sav")
        predictions = loaded_model.predict(new_predict_converted)

        return jsonify({"message": "process has been done successfully", "prediction": str(predictions[0])})

if __name__ == '__main__':
    app.run(debug=True)




    # curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/api

