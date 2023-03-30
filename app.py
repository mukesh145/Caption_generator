import streamlit as st
from PIL import Image
from io import StringIO
import pandas as pd
from generate1 import generate

def main():
    image = Image.open("static/priv2.png")
    logo = Image.open("static/icon.png")
    st.set_page_config(page_title="Image Caption Generator", page_icon=logo)

    st.image(image)
    st.title("Neural image caption generator")

    st.sidebar.title("Neural image caption generator")


    
    uploaded_file = st.file_uploader("Choose a file",type=['jpg'])
    if uploaded_file is not None:
        caption= generate(uploaded_file)
        with st.expander("see output"): 
            st.image(uploaded_file, caption)
if __name__ == "__main__":
    main()