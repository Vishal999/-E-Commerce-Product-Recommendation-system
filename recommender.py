from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def create_similarity_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    id_to_index = pd.Series(df.index, index=df['id'].astype(str)).to_dict()
    return cosine_sim, id_to_index

def recommend_products(product_id, df, cosine_sim, id_to_index, top_n=5):
    if product_id not in id_to_index:
        return []
    idx = id_to_index[product_id]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommendations = []
    for i, score in sim_scores:
        rec = df.iloc[i].to_dict()
        rec['similarity_score'] = round(score, 4)
        recommendations.append(rec)
    return recommendations
