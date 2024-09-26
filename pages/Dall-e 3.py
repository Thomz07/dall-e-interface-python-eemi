import streamlit as st
import openai

st.title("Le truc Dall-E là")

input_OpenAIKEY = st.text_input("Entrez votre clé API", type="password")
prompt = st.text_input("Veuillez entrer un prompt pour créer une image")

def prompt_dall_e():
    openai.api_key = input_OpenAIKEY

    if not openai.api_key:
        st.error("Veuillez entrer votre clé API.")
        return
    if not prompt:
        st.error("Veuillez entrer un prompt.")
        return

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
        )
        image_url = response['data'][0]['url']
        st.image(image_url, caption="Image générée par DALL·E")
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image: {e}")

if st.button("Générer l'image"):
    prompt_dall_e()
