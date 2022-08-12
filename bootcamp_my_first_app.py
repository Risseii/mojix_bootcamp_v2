import streamlit as st
st.write('Hello from the Mojix Bootcamp')
result = st.button('Click here')
if result:
    st.write(':smile:')

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.write('Simple but effective tips for every python lovers')

from PIL import Image
image = Image.open('imagen.jpg')

st.image(image, caption='Photo by Miesha Maiden from Pexels')

