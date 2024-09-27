from transformers import pipeline
from PIL import Image, ImageEnhance
import cv2
import numpy as np

# Load OCR pipeline
ocr_pipeline = pipeline("image-to-text", model="microsoft/trocr-base-printed")

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Adjust this factor as needed

    # Convert to numpy array for OpenCV processing
    image = np.array(image)

    # Rotate the image slightly if needed (adjust the angle)
    # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Denoise the image
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)

    # Apply binary thresholding
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Convert back to PIL image
    image = Image.fromarray(image)

    # Resize the image to a fixed size to normalize input
    image = image.resize((800, 800), Image.LANCZOS)  # Resize to 800x800

    return image

def ocr_function(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Preprocess the image
    image = preprocess_image(image)

    # Extract text from the image
    extracted_text = ocr_pipeline(image, max_new_tokens=50)  # Process the image with the OCR model
    return extracted_text[0]['generated_text']  # Access the generated text

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\simran\OneDrive\Desktop\ocr2.jpg"  # Set your image path here
    text = ocr_function(image_path)  # Call the OCR function
    print("Extracted Text:", text)
