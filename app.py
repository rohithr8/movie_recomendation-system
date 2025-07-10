import pickle
import pandas as pd
import streamlit as st
import requests

# --- Fetch poster from TMDB ---
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    )
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# --- Recommend movies ---
def recommend(movie):
    recommended_movies = []
    recommended_posters = []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    for i in movie_list:
        movie_title = movies.iloc[i[0]].title
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# --- Streamlit app ---
st.title('Movie Recommendation System')

# Load data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown
option = st.selectbox(
    "We recommend movies based on your interest",
    movies['title'].values
)

# Button
st.button("Clear", type="primary")

if st.button("Recommendations"):
    names, posters = recommend(option)

    for i in range(0, 6, 3):  # Display in two rows of three columns
        col1, col2, col3 = st.columns(3)

        with col1:
            if i < len(names):
                st.header(names[i])
                st.image(posters[i])

        with col2:
            if i + 1 < len(names):
                st.header(names[i + 1])
                st.image(posters[i + 1])

        with col3:
            if i + 2 < len(names):
                st.header(names[i + 2])
                st.image(posters[i + 2])
