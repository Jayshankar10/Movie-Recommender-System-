import streamlit as st
import pandas as pd
import os
import pickle
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]    
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie
         


st.title("Movie Recommendation System")

movies_dict = pickle.load(open('Notebook/movies.pkl','rb'))
similarity = pickle.load(open('Notebook/similarity_metrix.pkl','rb'))
movies = pd.DataFrame(movies_dict)
Selected_movies_name = st.selectbox(  
                     "Please select the movie name",                      
                      movies['title'].values
                     )

if st.button("Recommend Movies"):
    recommendation = recommend(Selected_movies_name)
    for i in recommendation:
        st.write(i)



st.balloons()


