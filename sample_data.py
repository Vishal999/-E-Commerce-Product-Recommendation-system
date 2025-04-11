import os
import pandas as pd


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

# Convert to DataFrame
df_sample = pd.DataFrame(sample_data)

# Step 3: Create directory and save new CSV
os.makedirs("amazon_data", exist_ok=True)
df_sample.to_csv(csv_path, index=False)
print("New sample data saved to CSV.")

# Step 4: Define function to load and clean the product data
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

    # Calculate popularity score from rating count
    df['rating_count'] = df['rating_count'].replace(',', '', regex=True).astype(float)
    df['popularity_score'] = df['rating_count'] / df['rating_count'].max() * 10

    return df[['id', 'name', 'description', 'category', 'popularity_score']]

# Step 5: Run the function and print the result
print("\nProcessed Product Data:")
print(get_product_data())

