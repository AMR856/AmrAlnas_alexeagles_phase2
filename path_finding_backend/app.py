#!/usr/bin/env python3
import os
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound, InternalServerError, Conflict
from .views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app)

@app.errorhandler(404)
def not_found(err: NotFound) -> str:
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(409)
def conflict(err: Conflict) -> str:
    return jsonify({'Error': 'Conflict of states was made'}), 409

@app.errorhandler(500)
def not_found(err: InternalServerError) -> str:
    return jsonify({"error": "The server has something weird going on"}), 500

if __name__ == '__main__':
    host = os.getenv("API_HOST", '0.0.0.0')
    port = os.getenv('API_PORT', 3000)
    app.run(host=host, port=port, debug=True)
