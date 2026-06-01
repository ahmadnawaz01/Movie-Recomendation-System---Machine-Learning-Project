# 🎬 Movie Recommender System

### 🌐 Live Web App: (https://movie-recomendation-system---machine-learning-project-3shsnryt.streamlit.app/)

A sleek, minimal, and aesthetic Content-Based Movie Recommendation System built using Machine Learning and Python. The application analyzes movie metadata—including genres, keywords, cast, crew, and overviews—to instantly recommend 5 similar movies. It features a clean, poster-first user interface that fetches dynamic artwork directly from the official TMDB API in real-time.

---

## 🛠 Tech Stack & Tools
* **Language:** Python
* **Machine Learning & Data Processing:** Scikit-learn, Pandas, NumPy, Joblib
* **Text Processing (NLP):** NLTK (Porter Stemming, Tokenization)
* **Web Framework:** Streamlit
* **API Integration:** TMDB API (The Movie Database)

---

## ⚙️ Core Architecture & Workflow

1. **Data Engineering:** Merged the TMDB 5000 Movies and Credits datasets, filtering down to key structural features like `movie_id`, `title`, `genres`, `keywords`, `cast`, and `crew`.
2. **Feature Text Processing:** Extracted the director from the crew list and top actors from the cast. Cleaned, tokenized, and applied stemming to all metadata strings to consolidate them into a single, uniform vector of "tags".
3. **Vectorization (Bag of Words):** Converted text tags into a 5000-dimensional numerical space using `CountVectorizer`.
4. **Similarity Engine:** Computed a **Cosine Similarity Matrix** to calculate the exact spatial geometric distance between all movie vectors.
5. **Storage Optimization:** Optimized a 176 MB raw similarity matrix by utilizing `joblib` memory-mapping compression, shrinking it down to a lightweight deployment asset under GitHub's file limitations.

---
