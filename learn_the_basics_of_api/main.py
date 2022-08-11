# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}




