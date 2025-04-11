import streamlit as st
from sample_data import get_product_data
from recommender import create_similarity_matrix, recommend_products

st.set_page_config(page_title="Product Recommender", layout="wide")
st.title("🛒 AI-Based Product Recommender")
st.markdown("Get content-based product recommendations based on descriptions.")

df = get_product_data()
df['id'] = df['id'].astype(str)
cosine_sim, id_to_index = create_similarity_matrix(df)

selected_name = st.selectbox("Select a product to get recommendations:", df['name'].tolist())
selected_id = df[df['name'] == selected_name]['id'].values[0]

recommendations = recommend_products(str(selected_id), df, cosine_sim, id_to_index)

st.subheader(f"Top Recommendations for: {selected_name}")
for rec in recommendations:
    st.markdown(f"**{rec['name']}** ({rec['category']})")
    st.markdown(f"- _{rec['description']}_")
    st.markdown(f"🔍 Similarity Score: **{rec['similarity_score']}**")
    st.markdown("---")
