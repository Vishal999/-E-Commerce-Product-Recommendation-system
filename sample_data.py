
import random
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
random.seed(42)
np.random.seed(42)

# Generate sample users
def generate_users(num_users=100):
    users = []
    for user_id in range(1, num_users + 1):
        users.append({
            "user_id": user_id,
            "username": fake.user_name(),
            "email": fake.email(),
            "location": fake.city(),
            "signup_date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(users)

# Generate sample products
def generate_products(num_products=200):
    categories = ["Electronics", "Books", "Clothing", "Home", "Gaming", "Fitness", "Office", "Accessories"]
    products = []
    for product_id in range(1, num_products + 1):
        products.append({
            "product_id": product_id,
            "product_name": fake.catch_phrase(),
            "category": random.choice(categories),
            "price": round(random.uniform(5, 500), 2),
            "brand": fake.company(),
            "rating": round(random.uniform(1, 5), 1)
        })
    return pd.DataFrame(products)

# Generate sample interactions
def generate_interactions(users_df, products_df, num_interactions=1000):
    interactions = []
    interaction_types = ["view", "click", "add_to_cart", "purchase"]
    for _ in range(num_interactions):
        interactions.append({
            "user_id": random.choice(users_df["user_id"].tolist()),
            "product_id": random.choice(products_df["product_id"].tolist()),
            "interaction_type": random.choices(
                interaction_types,
                weights=[0.5, 0.3, 0.15, 0.05],  # more views, fewer purchases
                k=1
            )[0],
            "timestamp": fake.date_time_between(start_date='-1y', end_date='now')
        })
    return pd.DataFrame(interactions)

# Save datasets
def save_data():
    users = generate_users()
    products = generate_products()
    interactions = generate_interactions(users, products)

    users.to_csv("bithub_users.csv", index=False)
    products.to_csv("bithub_products.csv", index=False)
    interactions.to_csv("bithub_interactions.csv", index=False)
    print("✅ BitHub sample data saved.")

# Run directly
if __name__ == "__main__":
    save_data()
