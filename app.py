import streamlit as st
import pickle
import requests
import joblib

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = joblib.load('similarity.pkl')

movie_list = movies['title'].values

st.set_page_config(
    page_title="Movie Recommender", page_icon="🎬", layout="centered",
)

st.title("🎬 Movie Recommender System")


def fetch_pos(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a8f42c99dd8f4f1a54e6a201c138bac2&language=en-US"
    response = requests.get(url)
    data = response.json()
    path = data.get('poster_path')
    if path:
        return "https://image.tmdb.org/t/p/w500" + path
    else:
        return None


def recommend(movie):
    ind = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[ind])), reverse=True, key=lambda x: x[1])
    recommovies = []
    recommposters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommovies.append(movies.iloc[i[0]].title)
        recommposters.append(fetch_pos(movie_id))
    return recommovies, recommposters


selected_movie = st.selectbox("Select a movie",movie_list)


if st.button("Recommend"):
    moviena, moviepos = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(moviena[0])
        if moviepos[0]:
            st.image(moviepos[0])

    with col2:
        st.text(moviena[1])
        if moviepos[1]:
            st.image(moviepos[1])

    with col3:
        st.text(moviena[2])
        if moviepos[2]:
            st.image(moviepos[2])

    with col4:
        st.text(moviena[3])
        if moviepos[3]:
            st.image(moviepos[3])

    with col5:
        st.text(moviena[4])
        if moviepos[4]:
            st.image(moviepos[4])