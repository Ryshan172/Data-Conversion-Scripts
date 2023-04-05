import json

# Load the JSON data from file
with open('data.json', 'r') as f:
    data = json.load(f)

# Initialize the GeoJSON data structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Loop through each post and create a GeoJSON feature
for post in data["Posts"].values():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post["longitude"], post["latitude"]]
        },
        "properties": {
            "title": post["title"],
            "description": post["description"],
            "geolocation": f"{post['latitude']},{post['longitude']}",
            "image": post["picture"]
        }
    }
    geojson["features"].append(feature)

# Write the GeoJSON data to file
with open('data.geojson', 'w') as f:
    json.dump(geojson, f)
