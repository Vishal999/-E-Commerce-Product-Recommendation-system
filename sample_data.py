import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder

# ------------------------------
# Step 1: Define Products with Categories
# ------------------------------
products_data = {
    'product_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007'],
    'product_name': [
        'Wireless Mouse', 'Sports Shoes', 'Cotton T-Shirt',
        'Smartphone', 'Blender', 'Organic Apple', 'Bluetooth Speaker'
    ],
    'category': [
        'Electronics', 'Fashion', 'Fashion',
        'Mobiles', 'Home Appliances', 'Groceries', 'Electronics'
    ],
    'brand': [
        'Logitech', 'Nike', 'H&M',
        'Samsung', 'Philips', 'Whole Foods', 'boAt'
    ],
    'price': [25, 60, 20, 300, 45, 5, 40]
}

products_df = pd.DataFrame(products_data)

# ------------------------------
# Step 2: Encode Features for Similarity
# ------------------------------
product_features = products_df[['category', 'brand']]
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(product_features).toarray()

# Optional: add price category (low/medium/high)
def price_category(price):
    if price <= 20:
        return 'low'
    elif price <= 100:
        return 'medium'
    else:
        return 'high'

products_df['price_category'] = products_df['price'].apply(price_category)
price_encoded = OneHotEncoder().fit_transform(products_df[['price_category']]).toarray()

# Combine all features
import numpy as np
combined_features = np.hstack((encoded_features, price_encoded))

# ------------------------------
# Step 3: Compute Content Similarity
# ------------------------------
content_similarity = cosine_similarity(combined_features)

# Make DataFrame with product_ids
product_similarity_df = pd.DataFrame(
    content_similarity,
    index=products_df['product_id'],
    columns=products_df['product_id']
)

# ------------------------------
# Step 4: Recommend Similar Products
# ------------------------------
def recommend_similar_products(product_id, top_n=3):
    if product_id not in product_similarity_df.columns:
        return "Product not found!"
    similar_scores = product_similarity_df[product_id].sort_values(ascending=False)[1:top_n+1]
    return products_df[products_df['product_id'].isin(similar_scores.index)][['product_name', 'category', 'brand']]

# ------------------------------
# Example Usage
# ------------------------------
print("🔁 Products similar to 'Smartphone' (P004):")
print(recommend_similar_products("P004"))
