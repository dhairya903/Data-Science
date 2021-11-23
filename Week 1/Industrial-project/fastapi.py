from PIL import Image
from fastapi import FastAPI, Path, HTTPException
import re
import pytesseract
import os

app = FastAPI()

cwd = os.getcwd()
cwd += '\\Industrial-project\\'

@app.get("/")
def home():
    return {"Home page": "Success"}

@app.get("/total-amount/{filename}")
def get_total_amount(filename: str = Path(..., description='Path of the invoice file')):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # To get the string fromat of the image
    filepath = cwd + filename
    try:
        image_str = pytesseract.image_to_string(Image.open(filepath))
        print(image_str)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Please enter correct file name or check path settings.")
        # return {'FileNotFoundError':'Please enter correct file name or check path settings.'}
    # Remove all the spaces from the string
    nospaces = "|".join(image_str.split())
    # Remove all the comma's from the amounts
    text = nospaces.replace(',', '')
    print(text)
    # Get the list of all amounts in the file
    amounts = re.findall('[-+]?([0-9]+\.[0-9]*)', text)
    # Convert amounts from string to float
    amounts = [float(x) for x in amounts]
    # Find the maximum of the amounts
    max_amount = max(amounts)
    return {'Total amount': max_amount}
