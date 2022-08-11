# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

course_items = {1: "Python", 2: "NodeJS", 3: "Machine Learning"}

@app.get("/courses/{course_id}")
def read_courses(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q}
    return {"course_name": course_items[course_id]}
