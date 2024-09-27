OCR Web App
This project is a basic OCR (Optical Character Recognition) web app that lets you upload images, extract text from them, and search for words within the text. It’s built using Streamlit (a tool to create web apps in Python) and Tesseract.
1. Setting Up the Project (Windows):
NEEDS:
    1:Python 
    2:Tesseract OCR (software to read text from images)
    3:Git 

Step 1: Download the Project
Commandprompt :
 git clone https://github.com/your-username/ocr_project.git
 cd ocr_project
 
Step 2: Create a Virtual Environment
A virtual environment is like a sandbox where you can install packages safely.
Commandprompt :
python -m venv ocr_env
ocr_env\Scripts\activate

Step 3: Install Necessary Packages
Commandprompt :
pip install -r requirements.txt

Step 4: Set Up Tesseract
Find the Tesseract file on your computer.
  python
import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

2. Running the App
Step 1: Activate the Environment

In Command Prompt, go to your project folder and run:

Commandprompt :

ocr_env\Scripts\activate

Step 2: Start the Web App

To open the app, run:

Commandprompt :

streamlit run app.py

The app will open in your browser at http://localhost:8501. Now, you can upload an image and extract text from it.
3. Optional: Deploying the App

If you want to put the app online so others can use it:
Option 1: Using Streamlit Cloud
   Create a Streamlit account at Streamlit.io.
    Link your GitHub project.
    Deploy the app directly.

4. Common Problems

    Tesseract not working: Make sure Tesseract is installed, and the correct path is set.
    Missing packages: Run pip install -r requirements.txt if any libraries are missing.

5. Project Layout

Here’s what the project looks like:

bash

ocr_project/
├── app.py                # Main web app code
├── ocr_integration.py     # (Optional) Code for OCR functions
├── requirements.txt       # List of tools and libraries
└── README.md              # Instructions for using the project

