from flask import Flask, render_template, request, jsonify
import subprocess
import os
import pandas as pd
from KMeans import get_nearby_restaurants
import joblib

app = Flask(__name__)

#here we define our flask routes which are called in the java script that controls the website, these routes refrence other scripts that we have in the main directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graph', methods=['POST'])
def api_generate_graph():
    data = request.get_json()
    zip_code = data.get('zipCode')
    demographic_type = data.get('demographicType')

    graph_filename = f"{demographic_type}_{zip_code}.png"
    script_name = 'generate_demographic_graph.py'
    
    os.makedirs('static/graphs', exist_ok=True)
    
    subprocess.run(['python', script_name, zip_code, demographic_type, f'static/graphs/{graph_filename}'])
    return jsonify(success=True, graphFilename=graph_filename)


@app.route('/get_nearby_restaurants', methods=['POST'])
def api_get_nearby_restaurants():
    data = request.get_json()
    restaurant_type = data.get('restaurantType')
    latitude = float(data.get('latitude'))
    longitude = float(data.get('longitude'))

    output_path = f'static/data/{restaurant_type.replace(" ", "_")}.csv'
    params, status_code = get_nearby_restaurants(restaurant_type, latitude, longitude, output_path)
    
    if status_code == 200:
        # read the clustered data to return it as JSON
        clustered_data = pd.read_csv(output_path)
        return jsonify({
            "success": True,
            "clusters": clustered_data.to_dict(orient="records")
        })
    else:
        return jsonify({
            "success": False,
            "message": params.get("message")
        }), status_code

#this is necessary for render deployment but most of our testing is done locally through flask 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

