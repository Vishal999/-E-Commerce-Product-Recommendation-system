import pandas as pd
 
 def get_product_data():
     data = {
         'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'name': [
             'Laptop Pro X', 'Wireless Mouse G', 'Mechanical Keyboard K', '4K Monitor Z',
             'Smartphone S10', 'Noise Cancelling Headphones H', 'Smartwatch W2',
             'Portable SSD P', 'Gaming Chair C', 'Webcam V5'
         ],
         'description': [
             'High performance laptop for professionals. Fast CPU and GPU.',
             'Ergonomic wireless mouse with long battery life. Precise tracking.',
             'RGB mechanical keyboard with tactile switches. Great for gaming.',
             'Stunning 27-inch 4K monitor with HDR support. Excellent colors.',
             'Latest generation smartphone with amazing camera and display.',
             'Over-ear headphones with active noise cancellation. Immersive audio.',
             'Feature-rich smartwatch with fitness tracking and notifications.',
             'Fast and reliable 1TB portable solid state drive. USB-C interface.',
             'Comfortable gaming chair with lumbar support and adjustable armrests.',
             'Full HD 1080p webcam with built-in microphone. Clear video calls.'
         ],
         'category': [
             'Electronics', 'Accessories', 'Accessories', 'Electronics',
             'Electronics', 'Accessories', 'Wearables',
             'Storage', 'Furniture', 'Accessories'
         ],
         'popularity_score': [8, 7, 6, 9, 10, 8, 7, 5, 6, 7]
     }
     return pd.DataFrame(data)
