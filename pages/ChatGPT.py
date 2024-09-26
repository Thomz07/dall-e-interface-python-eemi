import streamlit as st
from openai import OpenAI

st.title("ChatGPT")

input_OpenAIKEY = st.text_input("Entrez votre clé API")
st.write(input_OpenAIKEY)
prompt = st.text_input("Veuillez entrer un prompt")

def prompt_chatgpt():
    client = OpenAI(api_key=input_OpenAIKEY)

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"Tu es un traducteur de langue qui traduit de l'anglais vers le français." +" Si le texte en entrée n'est pas en anglais, tu retournes la phrase : 'Je ne prends que du texte en anglais.'"
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model="gpt-3.5-turbo",
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Erreur lors de la génération du texte : {e}")

if st.button("Générer le texte"):
    prompt_chatgpt()
