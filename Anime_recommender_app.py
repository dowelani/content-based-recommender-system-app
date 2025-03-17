import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import base64
import gzip
import surprise

# Set page configuration with a wide layout and custom title/icon
naruto_icon_path = os.path.join("Images", "pikachu_icon.png")
st.set_page_config(page_title="Anime Recommender System", page_icon=naruto_icon_path, layout="wide")

# Function to convert image to base64
def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load the icons
left_icon_path = os.path.join("Images", "left_icon.png")  
right_icon_path = os.path.join("Images", "right_icon.png")
home_icon_path = os.path.join("Images", "home_icon.png")
model_icon_path = os.path.join("Images", "model_icon.png")
data_icon_path = os.path.join("Images", "data_icon.png")
team_icon_path = os.path.join("Images", "team_icon.png")
pokemon_path = os.path.join("Images","pokemon.png")
left_icon_base64 = get_base64_image(left_icon_path)
right_icon_base64 = get_base64_image(right_icon_path)
home_icon_base64 = get_base64_image(home_icon_path)
model_icon_base64 = get_base64_image(model_icon_path)
data_icon_base64 = get_base64_image(data_icon_path)
team_icon_base64 = get_base64_image(team_icon_path)
pokemone_icon_base64 = get_base64_image(pokemon_path)

#App colour and design
st.markdown(f"""
    <style>
    /* Background colour*/
    .stApp {{
        background-color: #333333; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
        margin: 0;
        padding: 0;
        color: #fff;
    }}
    /* Header styling */
    h1 {{
        color: #fff; 
        text-align: center;
        text-shadow: 2px 2px 4px #ff1493;
        font-size: 48px;
        margin-top: 0px;
    }}
    h2 {{
        color: #fff; 
        text-shadow: 1px 1px 3px #ff4500;
    }}
    h3 {{
        color: #fff; 
    }}
    .st-emotion-cache-ue6h4q {{
        color: #fff;
    }}
    .st-bq {{
     color: #fff;;
    }}
    .st-hv {{
    color: rgb(49, 51, 63);
    }}
    .st-e5 {{
    background-color: #fff;
    }}
    .st-c1{{
    color: #ba9f0f
    }}
    element.style {{
    text-align: center;
    color: #fff;
    padding: 50px;
    }}
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: #C71585;
        padding: 10px;
        position: fixed; 
        top: 0;
        left: 0; /* Align to left edge */
        width: 100%; /* Full width of the page */
        display: flex;
        justify-content: space-around;
        z-index: 1000; /*  ensure tabs stay above content */
        margin: 10;
        box-sizing: border-box;
        transition: top 0.3s ease;  
    }}
    /* Individual tabs - Orchid color */
    .stTabs [data-baseweb="tab"] {{
        color: #fff; 
        font-weight: bold;
        padding: 90px 20px 5px 40px;
        background-color: #C71585; /* Orchid */
        transition: all 0.3s ease;
        flex-grow: 1;
        display: flex; /* Use flexbox for vertical alignment */
        flex-direction: column; /* Stack content vertically */
        justify-content: flex-end; /* Align text to bottom */
        text-align: center;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background-color: #C71585; /* Medium Violet Red */
        transform: scale(1.05);
    }}
    .stTabs [data-baseweb="tab-highlight"] {{
        background-color: #ffd700 !important; /* Gold */
        color: #fff; /*  white */
    }}
    /* Content area - Ensure it stays below tabs */
    .content {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 3px;
        border-radius: 0px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin: 0;
        color: #fff;
        position: relative; /* Ensure it respects document flow */
        z-index: 1; /* Lower than tabs */
    }}
    /* Button styling - Size, color, alignment */
    .stButton > button {{
        background-color: #FFD700; /* Gold */
        color: #fff; /* White text */
        padding: 12px 24px; /* Larger size: 12px vertical, 24px horizontal */
        font-size: 16px; /* Text size */
        border: none; /* Remove default border */
        border-radius: 8px; /* Rounded corners */
        width: 15%; /* Full width within container */
        text-align: center; /* Center text inside button */
        display: block; /* Ensures full-width behavior */
        margin: 10px auto; /* Center-align button horizontally */
        cursor: pointer; /* Hand cursor on hover */
        transition: background-color 0.3s ease; /* Smooth color transition */
    }}
    .stButton > button:hover {{
        background-color: #FFA500; /* Orange on hover */
    }}
    /* Style for the specific button */
    .custom-explore-button button {{
        background-color: #FF4500; /* Orange Red */
        color: #fff; /* White text */
        padding: 35px 35px; /* Size: 10px vertical, 20px horizontal */
        font-size: 32px; /* Text size */
        border: 2px solid #FFD700; /* Remove default border */
        border-radius: 45px; /* Rounded shape */
        width: 400px; /* Fixed width */
        text-align: center; /* Center text inside button */
        display: block; /* Block-level for width control */
        margin: 40px auto; /* Align left (adjust as needed) */
        cursor: pointer; /* Hand cursor on hover */
        transition: background-color 0.3s ease, transform 0.2s ease; /* Smooth transitions */
    }}
    .custom-explore-button button:hover {{
        background-color: #FF6347; /* Lighter orange on hover */
        transform: scale(1.05); /* Slight scale-up on hover */
    }}
    
    /* Add padding to the main container to push content below tabs */
    [data-testid="stAppViewContainer"] {{
        padding-top: 60px !important; /* Space for tab bar height */
        margin-top: 0 !important;
    }}
    /* Ensure no extra space above tabs */
    body {{
        margin: 0;
        padding: 0;
        color: #fff;
    }}
    </style>
    <!-- JavaScript for tab switching and debugging -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        setTimeout(function() {{
            var tabs = document.querySelectorAll('.stTabs [data-baseweb="tab-list"] button');
            console.log('Found tabs:', tabs.length);
            tabs.forEach(function(tab, index) {{
                console.log('Tab ' + index + ':', tab.innerText);
            }});
        }}, 1000);
    }});
    </script>
    
    """, unsafe_allow_html=True)

# Main function
def main():
    
    # Create tabs at the top
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Content Recommender","About the models", "About the data","About the team"])

    # Home Tab
    with tab1:
        st.markdown(
            f"""
            <h1>
                <img src="data:image/png;base64,{home_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-right: 10px;">
                Welcome to the Anime Universe!
                <img src="data:image/png;base64,{home_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-left: 10px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="content">', unsafe_allow_html=True)
        
        image_path = os.path.join("Images", "Home_page1.jpg")  
        st.image(image_path, use_container_width=True)
        
        st.write("Dive into the colorful world of anime! Explore epic adventures, heartwarming stories, and vibrant characters. This is your one-stop hub for all things anime!")
        st.write("So look no further and try our recommender system, to find the animes most suitable for you!")
        st.markdown("""
            <div class="custom-explore-button">
                <button onclick="document.querySelectorAll('.stTabs [data-baseweb=\"tab-list\"] button')[1].click()">Recommender System</button>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="custom-explore-button">', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Content Recommender Tab
    with tab2:
        st.markdown(
            f"""
            <h1>
                <img src="data:image/png;base64,{left_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-right: 10px;">
                Content Recommender
                <img src="data:image/png;base64,{right_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-left: 10px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write(" Have you ever finished an amazing anime and wished you had a list of equally exciting shows to watch next? That feeling of wanting more but not knowing where to start? 🎞️✨ That’s where our recommender system come in! It is like your personal anime guide, suggesting new shows and movies based on what you already love—so you’ll always have something awesome to watch next! Give it a try!")
        
        
        names = read_anime_data()
        algorithm = st.radio("Select an Algorithm:", ["Content Based Filtering", "Collaborative Based Filtering"])
        
        if algorithm == "Content Based Filtering":
        
            st.subheader("Please Select your favourite anime Title")
            anime_title = st.selectbox(" Anime Title:", names['name'])
                   
            if st.button("Recommend"):
                if anime_title:
                    results = content_recomm(anime_title)
                    #st.write("Recommendations:")
                    st.markdown(
                        f"""
                        <h3>
                            <img src="data:image/png;base64,{pokemon_icon_base64}" style="width: 30px; height: 30px; vertical-align: middle; margin-right: 10px;">
                            Recommendations:
                            <img src="data:image/png;base64,{pokemon_icon_base64}" style="width: 30px; height: 30px; vertical-align: middle; margin-left: 10px;">
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    for i, result in enumerate(results, 1):
                        st.write(f"{i}. {result}")
                else:
                    st.warning("Please select an anime.")
        else:
            st.subheader("Please Select your favourite anime Title")
            anime_title = st.selectbox(" Anime Title:", names['name'])

            if st.button("Recommend"):
                if anime_title:
                    title = names[names['name'] == anime_title]['anime_id'].iloc[0] 
                    results = collab_recomm(anime_title)
                    st.markdown(
                        f"""
                        <h3>
                            <img src="data:image/png;base64,{pokemon_icon_base64}" style="width: 30px; height: 30px; vertical-align: middle; margin-right: 10px;">
                            Recommendations:
                            <img src="data:image/png;base64,{pokemon_icon_base64}" style="width: 30px; height: 30px; vertical-align: middle; margin-left: 10px;">
                        </h3>
                        """,
                        unsafe_allow_html=True
                    )
                    #st.write("Recommendations:")
                    for i, result in enumerate(results, 1):
                        st.write(f"{i}. {result}")
                else:
                    st.warning("Please select an anime.")
                               
        st.markdown('</div>', unsafe_allow_html=True)
        
    # About the Model Tab
    with tab3:
        st.markdown(
            f"""
            <h1>
                <img src="data:image/png;base64,{model_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-right: 10px;">
                The Models!
                <img src="data:image/png;base64,{model_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-left: 10px;">
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write("The recommender system employs two distinct types of models, content based filtering and collaborative filtering. Each of these models use sophisticated machine learning algorithms and function  in a unique way to provide you a list of animes similar to your favourite anime title, for your  watch list.")
        
        st.markdown("<h2>Content Based Filtering</h2>", unsafe_allow_html=True)
        st.write("This recommender model is algorithm based. This means it does not use a predefined machine learning model, instead it is built from the ground up. The algorithm heavily relies on the mathametical concept of cosine similarity, which measures the cosine of the angle between two vectors in a multi-dimensional space. This metric is particularly useful for measuring how similar two items are in terms of their features, regardless of their magnitude. The model uses this concept to recommend anime titles based on their features and how similar they are to the title that is provided. To achieve this, each anime title is represented as a vector of features. these include the genre, type, number of members etc. Then the cosine similarity ois calculated between the title the user provides and over 12 000 animes in the our database. The anime titles with the highest cosine similarity are ranked higher and recommended to the user to watch next. However, this model has a slight drawback where it may recomend anime titles that are too similary to the one the user provided. Therefore lacking diversity. If you want recommendations that a nearly similar to your favourite anime, this is the model to choose!")
        #Image demonstrating cosine similarity to be inserted here
        st.markdown("<h2>Collaborative Filtering</h2>", unsafe_allow_html=True)
        st.write("This model, unlike content basd filtering, relies heavily on user prefernces and behaviour to identify anime titles suitable for recommendation. The model uses user-item interactions, which are the user anime ratings. It assumes that the user would like animes that a similar to those that other users who also watch the provided anime title like. Therefore, recommending the anime titles for the user to watch. The model creates a user-ratings matrix with the rows as users and columns as the anime titles, and their ratings for each user. Subsequently, the similarity score is calculated for each item and user. The model will find the users that have rated the provided anime title highly and recommend other animes that they have rated highly for the user to watch next. This ensures the modeel can identify complex patterns in user behaviour that werent obvious based on anime features alone. Consequently, it provides diversity recommendations. So, if you would like to get recommendations based on users like your self, this is you go to model! ")
        #Image show showcasing something similar to collaborative filtering
        st.markdown('</div>', unsafe_allow_html=True)
    # About the Data Tab
    with tab4:
        st.markdown(
            f"""
            <h1>
                <img src="data:image/png;base64,{data_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-right: 10px;">
                The Data!
                <img src="data:image/png;base64,{data_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-left: 10px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="content">', unsafe_allow_html=True)
        
        st.write("Two datasets were used to train our recommender models. One dataset contained all information regarding the animes, including the name, genres, types, number of episodes and average ratings. The second datset contained a list of users and their ratings for various anime titles. An analysis of these datasets highlighted some key information that i'd like to share with you!")
        
        st.markdown("<h2>Anime genres</h2>", unsafe_allow_html=True)
        st.write(" The bar chart reveals the most popular anime genres to be Comedy, Action, Adventure, Fantasy, and Sci-Fi. Yuri and Yaoi have the lowest popularity. majority of genres apprear less than 1000 times in the dataset.")
        image_path = os.path.join("Images", "genres.png")  
        st.image(image_path)
        
        st.markdown("<h2>Anime members popularity</h2>", unsafe_allow_html=True)
        st.write(" The bar chart reveals that most popular top 10 anime based on number of members range between 633.817k and 1.013917M with most of them falling bellow 717.796k number of members, it also shows that Death Note is the most popular anime based on number of members")
        image_path = os.path.join("Images", "members_pop.png")  
        st.image(image_path)
        
        st.markdown("<h2>Anime ratings popularity</h2>", unsafe_allow_html=True)
        st.write(" The bar chart below reveals that most popular top 10 anime based on average rating have high average ratings, which are between 9.16 and 10; Taka no Tsume 8: Yoshida-kun no X-Files has the highest avarage rating with a 10 average rating. This indicates that the highly rated animes, compared to the previous graph, are not necessarilly the most viewed. Death note is nowhere amongst the top 10 most rated. Similarly, the most rated animes where not in the most viewed plot")
        image_path = os.path.join("Images", "avg_ratings_pop.png")  
        st.image(image_path)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # About the Team Tab
    with tab5:
        st.markdown(
            f"""
            <h1>
                <img src="data:image/png;base64,{team_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-right: 10px;">
                Meet the team!
                <img src="data:image/png;base64,{team_icon_base64}" style="width: 45px; height: 45px; vertical-align: middle; margin-left: 10px;">
            </h1>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write("This app was brought to you by a team of dedicated Data Science students. ")
        st.markdown(f"""
                    * Nthabiseng Mokhachane
                    * Hope Mohola
                    * Khumbelo Dowelani
                    * Musa Khuzwayo
                    """,
            unsafe_allow_html=True
        )
        st.markdown("<h2>About This Site</h2>", unsafe_allow_html=True)
        st.write("""
            This site is built with love for anime fans! Created using Streamlit, 
            it showcases a colorful, interactive experience. Feel free to explore 
            and immerse yourself in the anime culture!
        """)
        st.markdown("**Created by:** A Team of Data Scientists | **Date:** March 06, 2025")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <footer style='text-align: center; color: #fff; padding: 20px;'>
            © 2025 Anime Recommender System | Powered by Streamlit ✨
        </footer>
    """, unsafe_allow_html=True)
        

#Reading anime data into script Function
def read_anime_data():
    names_N_id = pd.read_csv("Data/anime_names.csv")
    return names_N_id

#Content Based Recommender Function
def content_recomm(anime_title, top_n=10):
    title = anime_title
    with gzip.open('Model/cosine_similarity.pkl.gz', 'rb') as f:
        cosine_sim = pickle.load(f)
    with open('Model/indices.pkl', 'rb') as f:
        indices = pickle.load(f)
    with open('Model/anime_titles.pkl', 'rb') as f:
        anime_titles = pickle.load(f)

        # Get the index of the anime title
    idx = indices[anime_title]

    # Get the similarity scores for the anime title
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N similar anime titles
    sim_scores = sim_scores[1:top_n + 1]  # Exclude the anime itself

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the recommended anime titles
    results = anime_titles.iloc[anime_indices].tolist()
    
    return results


#Collaborative Recommender Function
def collab_recomm(anime_title,top_n=10):
    with gzip.open('Model/svd_model.pkl.gz', 'rb') as f:
        svd = pickle.load(f)
    with gzip.open('Model/train.pkl.gz', 'rb') as f:
        trainset = pickle.load(f)
        
    names = read_anime_data()
    
    anime_id = anime_title
    anime_users = trainset[trainset['anime_id'] == anime_id]['user_id']
    results = {}
    for _id in names['anime_id']:
      if _id != anime_id:
          pred = np.mean([svd.predict(u, _id).est for u in anime_users])
          results[_id] = pred
    
    top_n_ids = sorted(results, key=results.get, reverse=True)[:top_n]
    results = names[names['anime_id'].isin(top_n_ids)]['name'].tolist()
    return results
    
# Calling main function
if __name__ == "__main__":
    main()
