import osmnx as ox
import json
import hashlib

# Set the place name and retrieve data
place_name = "Zimbabwe"
gdf = ox.geometries_from_place(place_name, tags={'place': True})

# Convert the GeoDataFrame to a list of dictionaries
places = gdf[['name', 'geometry']].to_dict(orient='records')

# Function to generate a unique code for each place
def generate_unique_code(name, index):
    # Use the place name and index to create a unique hash
    unique_string = f"{name}-{index}"
    unique_code = hashlib.md5(unique_string.encode()).hexdigest()[:8].upper()
    return unique_code

# Convert geometries to longitude, latitude and add unique codes
for index, place in enumerate(places):
    if place['geometry'].geom_type == 'Point':
        place['longitude'] = place['geometry'].x
        place['latitude'] = place['geometry'].y
    else:
        place['longitude'] = place['geometry'].centroid.x
        place['latitude'] = place['geometry'].centroid.y
    del place['geometry']
    
    # Ensure place name exists
    place_name = place.get('name', f"Unnamed Place {index}")
    place['name'] = place_name
    
    # Generate a unique code
    place['code'] = generate_unique_code(place_name, index)

# Save the places data to a JSON file
with open('zimbabwe_places.json', 'w') as f:
    json.dump(places, f, indent=2)

print("Places data saved to 'zimbabwe_places.json'")
