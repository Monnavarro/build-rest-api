# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

from fastapi import FastAPI

app = FastAPI()

course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_course(start: int, end: int):
    return course_items [start: start + end]

