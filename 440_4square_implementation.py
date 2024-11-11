import requests
import pandas as pd
import numpy as np
import folium
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans

API_KEY = 'fsq34jULCzz+og3KIHasqw8qmGJEWm7eSjyJhI5Lg1/JcwY='
CLIENT_ID = "2J5UCCZPPORLG0ICMPVEP0JGHTJ2JGCN34TYQ0YLLQUIX0FL"
CLIENT_SECRET = "D3P0311L102QBXBAS3IGCVWIRBDAOMEVOGAZDZSYJMCORHGZ"
BASE_URL = 'https://api.foursquare.com/v3/places/search'.format(CLIENT_ID, CLIENT_SECRET)

def get_nearby_coffee_shops(latitude, longitude, radius, type):

    
    params = {
        "query": type,
        "ll": f"{latitude},{longitude}",
        "open_now": "true",
        "radius": radius,
        "sort": "DISTANCE",
        "limit": 50,  # Adjust this limit based on the API's maximum allowed per request
        "offset": 0   # Start with the first page
    }

    headers = {
        "Accept": "application/json",
        "Authorization": API_KEY
    }

    # Make the API request
    response = requests.get(BASE_URL, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        coffee_shops = []
        # Extract and print the relevant information


        for venue in results:
            name = venue.get('name', 'No Name')
            lat = venue.get('geocodes', {}).get('main', {}).get('latitude', 'No Latitude')
            lng = venue.get('geocodes', {}).get('main', {}).get('longitude', 'No Longitude')
            zip_code = venue.get('location', {}).get('postcode', 'No Zip Code')

            # Append the data as a dictionary to the list
            coffee_shops.append({
                "name": name,
                "latitude": lat,
                "longitude": lng,
                "zip_code": zip_code
            })
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    df = pd.DataFrame(coffee_shops)
    return df


latitude = 39.952583  # Replace with the desired latitude
longitude = -75.165222  # Replace with the desired longitude
radius = 10000  # Radius in meters




df = get_nearby_coffee_shops(latitude, longitude, radius,"Coffee Shops")


df['coordinates'] = df[['latitude', 'longitude']].values.tolist()

# Drop the original 'latitude' and 'longitude' columns
df = df.drop(columns=['latitude', 'longitude'])

# How many of this query type is in each of these zipcodes
restaurants_count= df.groupby('zip_code').count()
restaurants_count


df[['latitude', 'longitude']] = pd.DataFrame(df['coordinates'].tolist(), index=df.index)

# Step 2: Run k-means on latitude and longitude
k = 3  # Set the number of clusters you want
kmeans = KMeans(n_clusters=k, random_state=0)
df['cluster'] = kmeans.fit_predict(df[['latitude', 'longitude']])



# Insert the cluster labels at the beginning of the DataFrame
df.insert(0, 'Cluster labels', df['cluster'])

# Create a new DataFrame with only 'Cluster labels' and 'zip_code'
restaurants_clustering = df[['Cluster labels', 'coordinates']]

# Reset the index
restaurants_clustering.reset_index(drop=True, inplace=True)

# Sort by 'zip_code'
restaurants_clustering.sort_values(by='coordinates', inplace=True)

