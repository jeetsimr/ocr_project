import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Function to perform OCR with preprocessing for different font sizes
def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert("L")

    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Adjust contrast, 2 is a good starting point

    # Apply a median filter to remove noise
    image = image.filter(ImageFilter.MedianFilter())

    # Resize the image to improve OCR accuracy for small fonts
    image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)

    return image

# Function to perform OCR with Hindi and English language support
def ocr_function(image):
    # Preprocess the image before OCR
    preprocessed_image = preprocess_image(image)

    # Specify both English and Hindi languages (eng for English, hin for Hindi)
    text = pytesseract.image_to_string(preprocessed_image, lang='eng+hin')
    return text

# Streamlit app
def main():
    st.title("OCR Text Extraction and Search (Hindi & English Support)")

    # Upload an image file
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR
        with st.spinner("Extracting text..."):
            extracted_text = ocr_function(image)
            st.text_area("Extracted Text", value=extracted_text, height=200)

        # Keyword search
        keyword = st.text_input("Enter a keyword to search:")
        if keyword:
            if keyword.lower() in extracted_text.lower():
                st.markdown(f"**Search Result:** Keyword '{keyword}' found in the text!")
            else:
                st.markdown(f"**Search Result:** Keyword '{keyword}' not found in the text.")

if __name__ == "__main__":
    main()
