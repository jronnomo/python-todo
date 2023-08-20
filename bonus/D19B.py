import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")

def convert_image():
    uploaded_image = st.session_state["uploaded_image"]
    # Create Pillow image instance
    img = Image.open(uploaded_image)

    # Convert to grey scale
    grey_img = img.convert("L")

    # Display image
    st.image(grey_img)

with st.expander("Start Camera"):
    # Start camera
    camera_image = st.camera_input("Camera")

if camera_image:

    # Create Pillow image instance
    img = Image.open(camera_image)

    # Convert to grey scale
    grey_img = img.convert("L")

    # Display image
    st.image(grey_img)

uploaded_image = st.file_uploader(label="Choose an image to convert",
                                  key="uploaded_image",
                                  on_change=convert_image)