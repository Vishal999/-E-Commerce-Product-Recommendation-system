mport os
import pandas as pd


# Step 2: Create fresh sample product data
sample_data = {
    'product_id': ['101', '102', '103', '104'],
    'product_name': ['Wireless Mouse', 'Bluetooth Headphones', 'Smart Watch', 'USB-C Hub'],
    'about_product': [
        'A smooth wireless mouse with ergonomic design.',
        'Noise-cancelling over-ear headphones with Bluetooth 5.0.',
        'Fitness smart watch with heart rate monitor.',
        'Multi-port USB-C hub with HDMI and SD card reader.'
    ],
    'category': ['Electronics', 'Audio', 'Wearables', None],
    'rating_count': ['1,200', '2,500', '900', '600']
}

# Step 3: Convert to DataFrame
df_sample = pd.DataFrame(sample_data)

# Step 4: Create directory if it doesn't exist
os.makedirs("amazon_data", exist_ok=True)

# Step 5: Overwrite the CSV file with sample data
df_sample.to_csv(csv_path, index=False)
print("CSV file overwritten with new sample data.")

# Step 6: Define function to load and process data
def get_product_data():
    df = pd.read_csv(csv_path)

    # Rename relevant columns
    df = df.rename(columns={
        'product_id': 'id',
        'product_name': 'name',
        'about_product': 'description'
    })

    # Clean and prepare fields
    df['id'] = df['id'].astype(str)
    df['description'] = df['description'].fillna('')
    df['category'] = df['category'].fillna('General')

    # Compute popularity score
    df['rating_count'] = df['rating_count'].replace(',', '', regex=True).astype(float)
    df['popularity_score'] = df['rating_count'] / df['rating_count'].max() * 10

    return df[['id', 'name', 'description', 'category', 'popularity_score']]

# Step 7: Print processed product data
print("\nProcessed Product Data:")
print(get_product_data())
