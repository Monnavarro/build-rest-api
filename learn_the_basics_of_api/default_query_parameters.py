# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI

app = FastAPI()

course_items = [{"course_name": "python"}, {"course_name": "Node JS"}, {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_course(start: int = 0, end: int = 10):
    return course_items[start: start + end]

