# Zimbabwe Places Data Generator

This project retrieves and processes geographic data for places in Zimbabwe using the `osmnx` library, and generates a JSON file containing detailed information about each place, including a unique code for each place.

## Features

- **Place Data Retrieval**: Uses the `osmnx` library to fetch geographic data for places in Zimbabwe.
- **Unique Code Generation**: Each place is assigned a unique code based on its name and index, ensuring no duplicates.
- **Longitude and Latitude Extraction**: Converts geographic geometries to longitude and latitude coordinates.
- **Fallback for Missing Names**: Provides a fallback name for places that do not have a name.
- **JSON Output**: Saves the processed data to a JSON file.

## Prerequisites

- Python 3.x
- `osmnx` library
- `shapely` library
- `hashlib` library (built-in with Python)

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/anesu398/ZimPlaces.git
    cd zimbabwe-places-data-generator
    ```

2. **Install the Required Libraries**:
    ```sh
    pip install osmnx
    ```

## Usage

1. **Run the Script**:
    ```sh
    python generate_places.py
    ```

2. **Output**:
   The script will generate a JSON file named `zimbabwe_places.json` containing the detailed place data.

## File Structure
 
 ZimPlaces/
├── Zimbabwe.py # Main script to generate the places data
├── zimbabwe_places.json # Output JSON file with place data (generated)
└── README.md # Project documentation

## Script Details

### `generate_places.py`

This script performs the following tasks:

1. **Set the Place Name and Retrieve Data**:
    ```python
    place_name = "Zimbabwe"
    gdf = ox.geometries_from_place(place_name, tags={'place': True})
    ```

2. **Convert GeoDataFrame to List of Dictionaries**:
    ```python
    places = gdf[['name', 'geometry']].to_dict(orient='records')
    ```

3. **Generate Unique Codes and Convert Geometries**:
    ```python
    for index, place in enumerate(places):
        if place['geometry'].geom_type == 'Point':
            place['longitude'] = place['geometry'].x
            place['latitude'] = place['geometry'].y
        else:
            place['longitude'] = place['geometry'].centroid.x
            place['latitude'] = place['geometry'].centroid.y
        del place['geometry']

        place_name = place.get('name', f"Unnamed Place {index}")
        place['name'] = place_name
        place['code'] = generate_unique_code(place_name, index)
    ```

4. **Save the Data to a JSON File**:
    ```python
    with open('zimbabwe_places.json', 'w') as f:
        json.dump(places, f, indent=2)
    ```

### `generate_unique_code` Function

This helper function generates a unique code for each place:
```python
def generate_unique_code(name, index):
    unique_string = f"{name}-{index}"
    unique_code = hashlib.md5(unique_string.encode()).hexdigest()[:8].upper()
    return unique_code
```
### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the MIT License.

### Contact

For any questions or suggestions, please contact ndabaprinco@gmail.com.