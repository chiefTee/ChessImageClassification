import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Chessman Classification")

st.title("Chessman Classification")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Convert image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=image.format)
    image_bytes = image_bytes.getvalue()

    # Predict button
    if st.button('Predict'):
        files = {'file': image_bytes}
        try:
            with st.spinner("Predicting..."):
                response = requests.post("http://127.0.0.1:8000/predict", files=files)
                response.raise_for_status()
                result = response.json()
                st.write(f"Predicted Class: {result['predicted_class']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")

# Instructions to run the Streamlit app
st.write("Run the following command in your terminal to start the Streamlit app:")
st.code("streamlit run src/app.py")
