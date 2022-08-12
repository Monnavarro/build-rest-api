# -- coding: utf-8 --
"""

Created on: 12/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_path = "test.png"
lang = "eng"
text = pytesseract.image_to_string(img_path, lang=lang)

print(text)

