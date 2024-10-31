import streamlit as st
import pytesseract
from PIL import Image

# Set the Tesseract executable path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("Capstone_09 Fall2024_OCR")

# Image upload UI in Streamlit
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    img = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img, lang='don-thuoc')  # Change 'eng' to 'don-thuoc' if you have a custom model

    # Display the extracted text
    st.write("**Extracted Text:**")
    st.write(text)
else:
    st.write("Please upload an image to extract text.")

