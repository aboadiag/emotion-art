from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from pyngrok import ngrok
import os
import numpy as np
import time
import requests
import json
import pandas as pd
# from collections import deque
from datetime import datetime
 

# Initialize Flask app
app = Flask(__name__)


# Enable CORS for all routes
CORS(app)

# Define the route for logging user data
@app.route('/logSliderData', methods=['POST'])
def log_Slider_data():

    try:
        data = request.json
        print(f"Raw data: {data}")

        action = data.get("action")
        timestamp_str = data.get("timestamp")


    #failed exception
    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"status": "error", "message": f"An error occured: {str(e)}"}), 500

    #success return
    return jsonify({"status": "success", "message": "Slider data logged successfully"}), 200

@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    # start_interaction() # intiialize the misty
    app.run(host="0.0.0.0", port=80) #flask should listen here