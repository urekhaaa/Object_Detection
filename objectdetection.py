import streamlit as st

st.set_page_config(
    page_title="AI Object Detection",
    page_icon="🔍"
)

st.title("🔍 AI Object Detection")

st.write("Welcome! Upload an image to detect objects.")

image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if image is not None:
    st.image(image, caption="Uploaded Image")