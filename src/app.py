#! /usr/bin/env python
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h3> Consul Mesh Gateway Multi-Cloud Demo <h3>"

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
