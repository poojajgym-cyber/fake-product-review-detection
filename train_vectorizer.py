import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

# ====== Sample training dataset ======
data = {
    "review": [
        "This product is very good and useful",
        "Worst product I have ever bought",
        "Excellent quality, totally worth it",
        "Fake item, waste of money",
        "Highly recommended, superb experience",
        "Do not buy, totally fake"
    ]
}

df = pd.DataFrame(data)

# ====== Train TF-IDF Vectorizer ======
vectorizer = TfidfVectorizer()
vectorizer.fit(df["review"])

# ====== Ensure 'model' folder exists ======
os.makedirs("../model", exist_ok=True)   # note: ../ means backend kku velila create aagum

# ====== Save vectorizer ======
with open("../model/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ tfidf_vectorizer.pkl created successfully in 'model/' folder")
