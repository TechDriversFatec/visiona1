from flask import request, jsonify
from controller import predict as predictController


def router(app):
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"name": "IA TALHAO"})

    @app.route('/predict', methods=['POST'])
    def predict():
        return predictController.predict(request)
