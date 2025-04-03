import streamlit as st

# Recipe data
recipe_data = {
    "recipe_name": "Millet Porridge (Koko)",
    "ingredients": [
        "1 cup millet flour",
        "4 cups water (or more for desired consistency)",
        "Sugar or honey to taste",
        "Milk (optional)",
        "Ginger (grated or powdered)",
        "Cloves (optional)",
        "Nutmeg (optional)",
        "Lemon zest (optional)"
    ],
    "preparation_text": """
    1.  In a bowl, mix the millet flour with a little water to form a smooth paste.
    2.  Boil the remaining water in a pot.
    3.  Gradually pour the millet paste into the boiling water, stirring constantly to avoid lumps.
    4.  Add ginger, cloves, and nutmeg (if using).
    5.  Continue stirring over medium heat until the porridge thickens.
    6.  Add sugar or honey to taste.
    7.  If desired, add milk and lemon zest.
    8.  Simmer for a few more minutes.
    9.  Serve hot.
    """,
    "video_path": "https://youtu.be/qoay33pXX6c?si=ybOkcYAawVjiBAKN",  # Updated video link
    "female_audio_path": "audios/female.mp3",
    "male_audio_path": "audios/male.mp3",
}

def display_text_recipe():
    st.subheader(recipe_data["recipe_name"])
    st.write("Ingredients:")
    for ingredient in recipe_data["ingredients"]:
        st.write("- " + ingredient)
    st.write("Preparation:")
    st.write(recipe_data["preparation_text"])

def display_video_recipe():
    if recipe_data["video_path"]:
        try:
            st.video(recipe_data["video_path"])  # Corrected line
        except Exception as e:
            st.error(f"Error displaying video: {e}")
    else:
        st.warning("Video path not provided.")

def display_audio_recipe():
    gender = st.radio("Select Voice Gender:", ("Female", "Male"))
    if gender == "Female":
        audio_path = recipe_data["female_audio_path"]
    else:
        audio_path = recipe_data["male_audio_path"]

    if audio_path:
        try:
            audio_file = open(audio_path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        except FileNotFoundError:
            st.error("Audio file not found. Please check the path.")
    else:
        st.warning("Audio path not provided.")

def main():
    st.title("Koko Diary")

    mode = st.radio("Select Mode:", ("Text", "Video", "Audio"))

    if mode == "Text":
        display_text_recipe()
    elif mode == "Video":
        display_video_recipe()
    elif mode == "Audio":
        display_audio_recipe()

if __name__ == "__main__":
    main()