import pandas as pd

# Load your dataset from the CSV file, stripping whitespace from headers and handling mixed types
data = pd.read_csv('merged dataset.csv', dtype=str).rename(columns=lambda x: x.strip())

# Convert Latitude and Longitude columns to numeric, forcing errors to NaN
data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')

# Drop any rows with missing or invalid Latitude/Longitude values
data.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Define the percentage of points to sample (between 20% and 30%)
sample_percentage = 0.01  # For example, 25%

# Function to sample points from each area
def sample_area(df, percentage):
    return df.sample(frac=percentage, random_state=1)  # Set a random_state for reproducibility

# Apply the sampling function to each group
sampled_data = data.groupby('Area').apply(sample_area, percentage=sample_percentage).reset_index(drop=True)

# Save the sampled data to a new CSV file
sampled_data.to_csv('sampled_dataset_1p.csv', index=False)

print(f"Sampled dataset saved as 'sampled_dataset_1p.csv' with {sample_percentage*100}% of points from each area.")
