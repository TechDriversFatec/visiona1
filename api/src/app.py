from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({"name":"IA TALHAO"})

@app.route('/predict',methods=['POST'])
def predict():
    content = request.json
    bands = {
        "b02": content["b02"],
        "b03":content["b03"],
        "b04":content["b04"],
        "b08":content["b08"]
    }
    return jsonify(bands)

if __name__ =="__main__":
    app.run(port=7500, host='0.0.0.0',  debug=True, threaded=True)
