# 🎬 Movie Recommendation System

A content-based movie recommender app built using **Python**, **Streamlit**, and **TMDB API**. This system suggests six similar movies based on a user's selection, complete with movie posters and a clean, responsive UI.

## 🚀 Features

- Recommend movies based on content similarity
- Fetch movie posters from The Movie Database (TMDB) API
- Display recommendations in a user-friendly layout
- Streamlit-powered interactive interface

## 🧠 How It Works

1. A movie is selected from a dropdown menu.
2. Cosine similarity is computed using preprocessed vectors stored in `similarity.pkl`.
3. Top 6 recommendations (excluding the selected movie) are fetched.
4. Poster images are retrieved using TMDB API.
5. Movies and posters are displayed using Streamlit columns.

## 📁 Project Structure

- `app.py`: Main Streamlit application
- `movies_dict.pkl`: Movie metadata (title, ID)
- `similarity.pkl`: Precomputed similarity matrix
- `requirements.txt`: Project dependencies

## 🛠️ Installation

```bash
git clone https://github.com/rohithr8/movie-recommender-streamlit.git
cd movie-recommender-streamlit
pip install -r requirements.txt
streamlit run app.py
