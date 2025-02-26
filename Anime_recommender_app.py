import streamlit as st
import pandas as pd
import pickle
import base64
import os

# Set page configuration with a wide layout and custom title/icon
st.set_page_config(page_title="Anime Recommender System", page_icon="🌸", layout="wide")

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
        margin-top: 60px;
    }}
    h2 {{
        color: #fff; 
        text-shadow: 1px 1px 3px #ff4500;
    }}
    h3 {{
        color: #fff; 
    }}
    .st-emotion-cache-ue6h4q {{
        color: #fff
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
        margin: 0;
        box-sizing: border-box;
        transition: top 0.3s ease;  
    }}
    /* Individual tabs - Orchid color */
    .stTabs [data-baseweb="tab"] {{
        color: #fff; 
        font-weight: bold;
        padding: 10px 20px;
        background-color: #C71585; /* Orchid */
        transition: all 0.3s ease;
        flex-grow: 1;
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
        padding: 2px;
        border-radius: 15px;
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

    
    """, unsafe_allow_html=True)

# Main function
def main():
    # Create tabs at the top
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Content Recommender","About the model", "About the data","About the team"])

    # Home Tab
    with tab1:
        st.markdown("<h1>🌟 Welcome to the Anime Universe! 🌟</h1>", unsafe_allow_html=True)
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write("Insert project overview here!")
        st.write("Dive into the colorful world of anime! Explore epic adventures, heartwarming stories, and vibrant characters. This is your one-stop hub for all things anime!")
        # Placeholder for an image (you can upload your own anime image)
        st.image("https://via.placeholder.com/600x300.png?text=Anime+Banner", caption="Epic Anime Adventure Awaits!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Content Recommender Tab
    with tab2:
        st.markdown("<h1>🌟 Content Recommender 🌟</h1>", unsafe_allow_html=True)
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.markdown("<h2>Top Anime Picks</h2>", unsafe_allow_html=True)
        
        algorithm = st.radio("Select an Algorithm:", ["Content Based Filtering", "Collaborative Based Filtering"])
        if algorithm == "Content Based Filtering":
        
            st.subheader("Enter Your Favourite Anime Title")
            anime_title = st.text_input("Anime Title:")
                   
            if st.button("Recommend"):
                if anime_title:
                    result = content_predict(anime_title)
                    st.write(result)
                else:
                    st.warning("Please fill select for all fields.")
        else:
            st.subheader("Enter Your User ID and Select Select your favourite anime Title")
            user_id = st.text_input("User ID:")
            anime_title = st.text_input("Anime Title:")

            if st.button("Recommend"):
                if user_id and anime_title:
                    result = Collab_predict(user_id,anime_title)
                    st.write(result)
                else:
                    st.warning("Please fill select for all fields.")
                               
        st.markdown('</div>', unsafe_allow_html=True)
        
    # About the Model Tab
    with tab3:
        st.markdown("<h1>🌟 The Model! 🌟</h1>", unsafe_allow_html=True)
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write("Insert info about the chosen model!")
        st.markdown('</div>', unsafe_allow_html=True)
    # About the Data Tab
    with tab4:
        st.markdown("<h1>🌟 The Data! 🌟</h1>", unsafe_allow_html=True)
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.markdown("<h2>About This Site</h2>", unsafe_allow_html=True)
        st.write("Insert EDA information to describe training data and soforth")
        st.markdown('</div>', unsafe_allow_html=True)

    # About the Team Tab
    with tab5:
        st.markdown("<h1>🌟 Meet the team! 🌟</h1>", unsafe_allow_html=True)
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.write("This app was brought to you by a team of dedicated Data Science students. ")
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
        

#Content Based Recommender Function
def predict(anime_title):
    with open('model/content_model.plk', 'rb') as f:
        model = pickle.load(f)

    return anime_recom


#Collaborative Recommender Function
def predict(user_id,anime_title):
    with open('model/collaborative_model.plk', 'rb') as f:
        model = pickle.load(f)

    return anime_recom
    
# Calling main function
if __name__ == "__main__":
    main()