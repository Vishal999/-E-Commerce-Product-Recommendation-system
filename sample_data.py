import pandas as pd

def get_product_data():
    csv_path = "amazon_data/amazon.csv"
    df = pd.read_csv(csv_path)

    # Rename relevant columns to match expected keys
    df = df.rename(columns={
        'product_id': 'id',
        'product_name': 'name',
        'about_product': 'description'
    })

    # Clean and prepare fields
    df['id'] = df['id'].astype(str)
    df['description'] = df['description'].fillna('')
    df['category'] = df['category'].fillna('General')

    # Create a popularity score based on rating_count (converted to int)
    df['rating_count'] = df['rating_count'].replace(',', '', regex=True).astype(float)
    df['popularity_score'] = df['rating_count'] / df['rating_count'].max() * 10

    # Select only required columns
    return df[['id', 'name', 'description', 'category', 'popularity_score']]
