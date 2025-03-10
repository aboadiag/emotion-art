from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
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


# Global container for artemis data set
artemis_df = None  # Global var with csv data
artemis_csv_fn = '../artemis_official_data/official_data/artemis_dataset_release_v0.csv'
wikiart_url = 'https://uploads7.wikiart.org/images/'

def artemis_painting_column_to_url(artemis_painting_name):
    # Take the strings from the painting column of the artemis dataset and turn it into a url
    artist_name, painting_name = artemis_painting_name.split('_')
    painting_url = '{}{}/{}.jpg'.format(wikiart_url, artist_name, painting_name)
    return painting_url

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


# Define the route for logging user data
@app.route('/getNewImage', methods=['POST'])
def get_new_image():
    try:
        data = request.json
        print(f"Raw data: {data}")

        action = data.get("action")
        timestamp_str = data.get("timestamp")
        user_id = data.get("userID")
        arousal = data.get("arousal")
        pleasure = data.get("pleasure")

    #failed exception
    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"status": "error", "message": f"An error occured: {str(e)}"}), 500

    # For now, just return the url to a random image in the artemis dataset
    ret_img = artemis_df.loc[np.random.randint(len(artemis_df)), 'painting']
    ret_img_url = artemis_painting_column_to_url(ret_img)

    return jsonify({
        "status": "success", 
        "message": "Slider data logged successfully",
        "img_url": ret_img_url
        }), 200

@app.route('/')
def index():
    # Just display the index.html file
    return render_template('index.html')


# Run the Flask app
if __name__ == "__main__":
    # Load artemis dataset to global variable
    try:
        artemis_df = pd.read_csv(artemis_csv_fn)
        print('Successfully loaded artemis data:')
        print(artemis_df.head())
        print(artemis_df.columns)
    except Exception as e:
        print('Could not load artemis data. Tried to load from filename: ', artemis_csv_fn)
        print(e)

    # start_interaction() # intiialize the misty
    app.run(debug=True, port=80) #flask should listen here
    