import streamlit as st
import openai

def prompt_dall_e():
    OpenAIKEY = st.session_state['input_OpenAIKEY']
    prompt = st.session_state['prompt']

    if not OpenAIKEY:
        st.error("Veuillez entrer votre clé API.")
        return
    if not prompt:
        st.error("Veuillez entrer un prompt.")
        return

    openai.api_key = OpenAIKEY

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
        )
        image_url = response['data'][0]['url']
        st.image(image_url, caption="Image générée par DALL-E 3")
    except Exception as e:
        st.error(f"Erreur lors de la génération de l'image: {e}")

st.title("Le truc Dall-E là")

# Use 'key' to store the input values in the session state
st.text_input("Entrez votre clé API", key='input_OpenAIKEY', type='password')
st.text_input("Veuillez entrer un prompt pour créer une image", key='prompt', on_change=prompt_dall_e)
