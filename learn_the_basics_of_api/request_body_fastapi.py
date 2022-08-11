# -- coding: utf-8 --
"""

Created on: 11/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None


app = FastAPI()

@app.post("/courses/")
def create_course(course: Course):
    return course

