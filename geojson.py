import folium
from folium import GeoJson

# Example polygons (replace with your actual polygons)
polygons = [
    [
        [23.789455600774247, 86.42845145302238],
        [23.78924943838375, 86.42845145302238],
        [23.78924943838375, 86.42913809852917],
        [23.789455600774247, 86.42913809852917],
        [23.789455600774247, 86.42845145302238]
    ],
    [
        [23.793824203481396, 86.42703524666223],
        [23.793823021697577, 86.42700895635221],
        [23.793819487727408, 86.42698291923368],
        [23.793813635605144, 86.42695738605967],
        [23.793805521690224, 86.4269326027299]
    ]
    # Add other polygons as needed
]

# Create a map
m = folium.Map(location=[23.79024233862799, 86.43735744994336], zoom_start=15)

# Function to handle popup with GeoJSON data
def on_polygon_click(e):
    geojson_data = e.target.to_geojson()
    print(geojson_data)  # This will print the GeoJSON data to the console

# Add polygons with click functionality to output GeoJSON
for i, polygon in enumerate(polygons):
    polygon_name = f"Polygon {i+1}"  # Name of the polygon

    # Adding polygons with custom properties
    folium.Polygon(
        locations=polygon,
        color='red',
        weight=5,
        fill=True,
        fill_color='red',
        fill_opacity=0.3,
        popup=f"Polygon {i+1}"
    ).add_to(m).add_child(folium.Popup(f"Polygon {i+1}"))

    # Adding GeoJSON with custom properties
    geojson_data = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": [polygon]},
            "properties": {
                "name": polygon_name,  # Custom property (polygon name)
                "area": 1000,  # Example: Add area as a property (you can replace with actual calculation)
                "type": "highlighted"  # Example: Add a type property
            }
        }]
    }

    geojson = folium.GeoJson(
        geojson_data,
        name="Polygon Layer"
    ).add_to(m)

    # Adding popup to GeoJSON with 'name' field from properties
    geojson.add_child(folium.GeoJsonPopup(fields=["name", "area", "type"], localize=True))

# Save and display the map
m.save("map_with_interactive_polygons.html")

# Display in notebook
from IPython.display import IFrame
IFrame("map_with_interactive_polygons.html", width=700, height=500)
m
