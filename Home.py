import streamlit as st
import random

st.title("Mon :blue[_formulaire_] super cool :sunglasses:")
st.write("Ceci est un formulaire de contact")

placeholders = ["Un magnifique kebab salade tomate oignon sauce algérienne biggy", "Une enorme boule de glace sur la tour eiffel", "Un mega plateau de sushi sur le golden gate bridge"]
st.text_input("Tapez votre prompt", placeholder=placeholders[random.randint(0,2)])