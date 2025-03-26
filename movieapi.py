import requests
import streamlit as st
import streamlit.components.v1 as components

# Access API key from Streamlit secrets
API_KEY = st.secrets["api"]["key"]

# Checking if it's importing correctly 
# st.write(API_KEY) 

# URLs
URLpopular = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

# UI
InputMovie = st.text_input("Enter your movie", placeholder="Movie Name")

if InputMovie:
    SearchUrl = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&include_adult=false&page=1&query={InputMovie}"

    responseInput = requests.get(SearchUrl)
    dataOfInput = responseInput.json()

    postnumber = 0
    # this is data -> results inside results ->top result poster_path
    if  len(dataOfInput["results"]) > 0 :
        imageURL = dataOfInput["results"][postnumber]["poster_path"] 
        imageTitle = dataOfInput["results"][postnumber]["title"]
        overview = dataOfInput["results"][postnumber]["overview"]
        rating = dataOfInput["results"][postnumber]["vote_average"]

        # printing data
        st.title(imageTitle)
        if imageURL:
            st.image("https://image.tmdb.org/t/p/w500" + imageURL)
        else:
            st.write("Image not available currently")

        st.markdown("**Overview:**  \n" + overview)
        st.write("Rating : ", rating)
   
        for i in range(1, 6):
            suggPostNum = i
            suggimageURL = dataOfInput["results"][suggPostNum]["poster_path"]
            suggimageTitle = dataOfInput["results"][suggPostNum]["title"]
            suggoverview = dataOfInput["results"][suggPostNum]["overview"]
            suggrating = dataOfInput["results"][suggPostNum]["vote_average"]

            if suggimageURL:
                st.image("https://image.tmdb.org/t/p/w92" + suggimageURL)
                st.markdown("**Overview:**  \n" + suggoverview)
    else :
        st.write("Movie is not available check the spelling or try again later...")



# Image configurations path here I got this from basics of tmdb api website

# check = f"https://api.themoviedb.org/3/configuration?api_key={API_KEY}"

# st.write(check)
