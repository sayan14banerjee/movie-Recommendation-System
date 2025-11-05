import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #2b5876, #4e4376);
            color: white;
        }
        .stSelectbox label {
            color: white !important;
        }
        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
            padding: 0.5rem 2rem;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #FF6B6B;
            border-color: #FF6B6B;
        }
        div[data-testid="stText"] {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 0.5rem;
            border-radius: 5px;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white; text-shadow: 2px 2px 4px #000000;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Add a brief description
st.markdown("""
    <p style='text-align: center; color: #E0E0E0; margin-bottom: 2rem;'>
        Discover movies similar to your favorites! Select a movie from the dropdown below and get personalized recommendations.
    </p>
""", unsafe_allow_html=True)
# Load the movie data and similarity matrix
movies = pickle.load(open('../models/movies.pkl', 'rb'))
similarity = pickle.load(open('../models/similarity.pkl', 'rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movie_list
)

def recomended_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recomendaed_movies_name = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recomendaed_movies_name.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recomendaed_movies_name, recommended_movies_posters
# Create a global session with retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=3,                # Retry up to 3 times
    backoff_factor=1,       # Wait 1s, 2s, 4s between retries
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = session.get(url, timeout=8)
        response.raise_for_status()  # Raises an error for bad responses
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=Poster+Not+Available"

    except requests.exceptions.RequestException as e:
        # Log the error but don't show repeated warnings to user
        print(f"⚠️ TMDb Fetch Error for ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"

if st.button("Show Recommendations"):
    recommended_movies_names, recommended_movies_posters = recomended_movies(selected_movie)   
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_posters[0]) 
    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_posters[2]) 
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_posters[3]) 
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_posters[4])