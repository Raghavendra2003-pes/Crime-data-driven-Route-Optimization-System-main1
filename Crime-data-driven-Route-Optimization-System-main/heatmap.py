import folium
import pandas as pd
from folium.plugins import HeatMap

# Load your dataset from the CSV file, stripping whitespace from headers and handling mixed types
data = pd.read_csv('sampled_dataset_1p.csv', dtype=str).rename(columns=lambda x: x.strip())

# Convert Latitude and Longitude columns to numeric, forcing errors to NaN
data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')

# Drop any rows with missing or invalid Latitude/Longitude values
data.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Create a map centered around the average location
if not data.empty:
    m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

    # Add points to the map
    for _, row in data.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']]).add_to(m)

    # Create a heatmap overlay
    HeatMap(data[['Latitude', 'Longitude']].values).add_to(m)

    # Save the map to an HTML file or display it
    m.save('sample_crime_map_1.html')
    print("ok")
else:
    print("No valid data to plot.")
