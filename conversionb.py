import json

with open('data.json') as f:
    data = json.load(f)

features = []
for post in data['Posts'].values():
    coordinates = post['coordinates'].split('; ')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude]
        },
        "properties": {
            "title": post['title'],
            "description": post['description'],
            "geolocation": f"{latitude}, {longitude}",
            "image": post['picture']
        }
    }
    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open('data.js', 'w') as f:
    f.write(f"var geojson = {json.dumps(geojson)};")
