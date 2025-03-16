# Anime Recommender System

![App Screenshot](https://raw.githubusercontent.com/dowelani/content-based-recommender-system-app/main/Images/Screenshot.jpg "Anime Recommender App")

## Table of Contents

- [1. Overview](#overview)
- [2. Recommender Systems](#recomm)
- [3. Application Structure](#appstruct)
- [4. Dependencies](#depen)
- [5. Environment Setup](#environment)
- [6. Team Members](#team-members)


## Overview
This repository contains a Streamlit web application that provides personalized anime recommendations using two approaches: **Collaborative Filtering** and **Content-Based Filtering**. The app is designed to help anime enthusiasts discover new titles based on user preferences and anime metadata.

## Recommender Systems
- **Collaborative Filtering**: Recommends anime based on user ratings and similarities between users.
- **Content-Based Filtering**: Suggests anime based on features like genres, themes, and descriptions.

## Application Structure
The application's interactive UI is built with Streamlit for easy input and visualization of recommendations. It contains several pages that immerse the user in the world of anime and recommender system. The pages contain the following:
* Home: A welcome page that informs the user about the purpose of the app and prompts them to try the recommender ssytem.
* Content recommender: A page that allows the user to try the recommender system. The user can select the type of model they want to use, and a dropdown menu where the user can select the anime they want recommendations from.
* About the models: Informs the user about the models behind the recomender app nand which one is most suitable for what
* About the data: Gives the user an overview of the data that was used to train the models, and provides key insights gained.
* About the team: Displays information regarding the team responsible for the application.

The application provides the user with a list of anime that they can watch based of the anime title thy choose on the dropdown menu. The application can be viewed [here.](https://content-based-recommender-system-app-gqh647vhctwvakqfzbiugn.streamlit.app/)

## Dependencies
The application relies on the following Python libraries:
- `streamlit` - For the web interface
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn` - Machine learning algorithms (e.g., cosine similarity)
- `requests` - For fetching external data (if applicable)
- `beautifulsoup4` - For web scraping or HTML parsing (if applicable)
- `pickle` - For loading pre-trained models

Install them using the provided `requirements.txt`:

## Environment Setup
### Local Setup
1. **Clone the Repository**:
   The first step to running this project is to clone the reposiory using the following commands:
   ```bash
   git clone https://github.com/dowelani/content-based-recommender-system-app.git
   cd content-based-recommender-system-app
    ```
2. **Create a virtual environment**
   You are encouraged to work within  a virtual environment, where you can install project requirements in isolation. To create your own virtual environment, load the following commands in the terminal. Replace `name_of_environment` with you desired name for the environment.
   ```bash
    conda create --name name_of_environment 
    conda activate name_of_environment
    ```
3. **Install dependencies**
   The aforementioned project dependencies are contained in the `requirements.txt`. The command below installs them into your environment, ensuring you have all the necessary packages to run the app locally.
   ```bash
    pip install -r requirements.txt
    ```
4. **Run app locally**
   The next part is to run the app locally. This is achieved by inputting the following command into the terminal. Ensure that you are in the directory for  cloned repository.
   
   ```bash
    streamlit run Anime_recommender_app.py
    ```

## Team Members
The following team members contributed to this project:

| Name                  | Email                                                                        |
| --------------------- | ---------------------------------------------------------------------------- |
| Motshabi Mohola       | [motshabimohola@gmail.com](mailto\:motshabimohola@gmail.com)                 |
| Khumbelo Dowelani     | [dowelanikhumbelo@gmail.com](mailto\:dowelanikhumbelo@gmail.com)             |
| Nthabiseng Mokhachane | [nthabisengmokhachane95@gmail.com](mailto\:nthabisengmokhachane95@gmail.com) |
| Musa Khuzwayo         | [musakhuzwayomedia@gmail.com](mailto\:musakhuzwayomedia@gmail.com)           |
