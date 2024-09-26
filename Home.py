import streamlit as st
import random

st.title("Mon :blue[_formulaire_] super cool :sunglasses:")
st.write("Ceci est un formulaire de contact")

placeholders = ["Un magnifique kebab salade tomate oignon sauce algérienne biggy", "Une enorme boule de glace sur la tour eiffel", "Un mega plateau de sushi sur le golden gate bridge"]
user_input = st.text_input("Tapez votre prompt")
st.write(user_input)

st.image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/19/a3/b0/l-original-pain-maison.jpg?w=1100&h=-1&s=1")

st.sidebar.title("Didier Deschamps")