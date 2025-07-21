import streamlit as st
import pandas as pd
import os
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=a7c0705e1a2faa59ef3d94cb9bddb7a1&language=en-US".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

    


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]    
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
          # Fetch movies poster ##

        
    return recommended_movie, recommended_movie_poster

         


st.title("Movie Recommendation System")

movies_dict = pickle.load(open('Notebook/movies.pkl','rb'))
similarity = pickle.load(open('Notebook/similarity_metrix.pkl','rb'))
movies = pd.DataFrame(movies_dict)
Selected_movies_name = st.selectbox(  
                     "Please select the movie name",                      
                      movies['title'].values
                     )

if st.button("Recommend Movies"):
    name,poster = recommend(Selected_movies_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])


st.balloons()


