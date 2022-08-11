# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/courses/{course_name}")
def red_course(course_name):
    return {"course name": course_name}

