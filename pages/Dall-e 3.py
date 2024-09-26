import streamlit as st
from openai import OpenAI

def prompt_dall_e(OpenAIKEY):

    client = OpenAI(api_key=OpenAIKEY)

    prompt = prompt

    image_cree = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="512x512",
        quality="standard",
        n=1,
    )

    st.image(image_cree)

st.title("Le truc Dall-E là")

input_OpenAIKEY = st.text_input("Entrez votre clé API")
prompt = st.text_input("Veuillez entrer un prompt pour créer une image", on_change=prompt_dall_e(input_OpenAIKEY))

