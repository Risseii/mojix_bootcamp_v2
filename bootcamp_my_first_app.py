import streamlit as st
st.write('Hello from the Mojix Bootcamp')
result = st.button('Click here')
if result:
    st.write(':smile:')

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.write('Simple but effective tips for every python lovers')

st.markdown(body, unsafe_allow_html=False)

from PIL import Image
image = Image.open('https://miro.medium.com/max/1400/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.image(image, caption='Photo by Miesha Maiden from Pexels')

