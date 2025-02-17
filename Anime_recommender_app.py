import streamlit as st
import pandas as pd
import pickle

# Main function
def main():
    page = st.sidebar.radio(" ", ["Home", "About the model","EDA", "Content Recommender","About the team"])

    # Set up content for each page
    if page == "Home":
        st.title("Welcome!")
        st.write("Insert project overview here!")
    elif page == "About the model":
        st.title("About the Model")
        st.write("Insert info about the chosen model!")
    elif page == "EDA":
        st.title("Exploratory Data Analysis")
        st.write("Insert EDA information to describe training data and soforth")
    elif page == "Content Recommender":
        st.title("Anime Content Recommender")

        algorithm = st.radio("Select an Algorithm:", ["Content Based Filtering", "Collaborative Based Filtering"])

        st.subheader("Enter Your Three favourite Movies")
        
        option_1 = st.text_input("First option:")
        option_2 = st.text_input("Second option:")
        option_3 = st.text_input("Third option:")
                
        if st.button("Recommend"):
            if option_1 and option_2 and option_3:
                result = predict(option_1,option_2,option_3,algorithm)
                st.write(result)
            else:
                st.warning("Please fill all the fields.")
        
    elif page == "About the team":
        st.title("Meet the team!")
        st.write("This app was brought to you by a team of dedicated Data Science students. ")

#Recommender function
def predict(movie1,movie2,movie3,algorithm):
    if algorithm == "Collaborative Based Filtering":
    
        with open('model/model.plk', 'rb') as f:
            model = pickle.load(f)
    else:
        model = something

    return anime_recom
    
# Calling main function
if __name__ == "__main__":
    main()