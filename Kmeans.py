from flask import Flask, request, jsonify
import requests
import pandas as pd
import folium
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans

API_KEY = 'fsq34jULCzz+og3KIHasqw8qmGJEWm7eSjyJhI5Lg1/JcwY='
BASE_URL = 'https://api.foursquare.com/v3/places/search'

app = Flask(__name__)

def get_nearby_restaurants(restaurant_type, latitude, longitude, output_path):
    
    params = {
        "query": restaurant_type,
        "ll": f"{latitude},{longitude}",
        "radius": 10000,  # Radius in meters
        "sort": "DISTANCE",
        "limit": 50,  # limit of businesses that we can get from four square
    }

    headers = {
        "Accept": "application/json",
        "Authorization": API_KEY
    }


    response = requests.get(BASE_URL, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        restaurants = []

        # extract and store the relevant information
        for venue in results:
            name = venue.get('name', 'No Name')
            lat = venue.get('geocodes', {}).get('main', {}).get('latitude', 'No Latitude')
            lng = venue.get('geocodes', {}).get('main', {}).get('longitude', 'No Longitude')
            zip_code = venue.get('location', {}).get('postcode', 'No Zip Code')

            restaurants.append({
                "name": name,
                "latitude": lat,
                "longitude": lng,
                "zip_code": zip_code
            })

        df = pd.DataFrame(restaurants)
        
       
        if df.empty:
            return jsonify({"message": f"No data found for restaurant type: {restaurant_type} at location ({latitude}, {longitude})"}), 404
        
        
        k = 3  # Set the number of clusters
        kmeans = KMeans(n_clusters=k, random_state=0)
        df['cluster'] = kmeans.fit_predict(df[['latitude', 'longitude']])
        
        df.to_csv(output_path, index=False)
        
        map_clusters = folium.Map(location=[latitude, longitude], zoom_start=12)
        
        x = np.arange(k)
        ys = [i + x + (i*x)**2 for i in range(k)]
        colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
        rainbow = [colors.rgb2hex(i) for i in colors_array]

        for lat, lon, cluster in zip(df['latitude'], df['longitude'], df['cluster']):
            folium.CircleMarker(
                [lat, lon],
                radius=5,
                popup=f'Cluster {cluster}',
                color=rainbow[cluster-1],
                fill=True,
                fill_color=rainbow[cluster-1],
                fill_opacity=0.7).add_to(map_clusters)

        map_file = f"{output_path.replace('.csv', '')}_map.html"
        map_clusters.save(map_file)
        
        return jsonify({"message": f"Data saved to {output_path}", "map_file": map_file}), 200
        
    else:
        return jsonify({"message": f"Error: {response.status_code}", "details": response.text}), response.status_code

@app.route('/get_nearby_restaurants', methods=['GET'])
def api_get_nearby_restaurants():
    restaurant_type = request.args.get('restaurant_type')
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    output_path = request.args.get('output_path')
    
    response = get_nearby_restaurants(restaurant_type, latitude, longitude, output_path)
    return response

if __name__ == '__main__':
    app.run(debug=True)






