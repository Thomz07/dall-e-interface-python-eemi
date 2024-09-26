import streamlit as st
from openai import OpenAI

st.title("Dall-E 3")

input_OpenAIKEY = st.text_input("Entrez votre clé API")
st.write(input_OpenAIKEY)
prompt = st.text_input("Veuillez entrer un prompt pour créer une image")

def prompt_dall_e():
    client = OpenAI(api_key=input_OpenAIKEY)

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            #size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response['data'][0]['url']
        st.image(image_url, caption="Image générée par DALL·E")
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image: {e}")

if st.button("Générer l'image"):
    prompt_dall_e()
