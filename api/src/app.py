from flask import Flask, request, jsonify
from router import router
import requests
import json
app = Flask(__name__)
router(app)

if __name__ == "__main__":
    app.run(port=7500, host='0.0.0.0',  debug=True, threaded=True)
