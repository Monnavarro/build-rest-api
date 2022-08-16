# -- coding: utf-8 --
"""

Created on: 12/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pytesseract

img_path = 'frase.png'
lang = 'eng'
text = pytesseract.image_to_string(img_path, lang=lang)

print(text)

