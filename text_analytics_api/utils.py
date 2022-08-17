# -- coding: utf-8 --
"""

Created on: 17/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import requests as req

def call_text_analytics_api(headers, document, endpoint):
    response = req.post(
        "https://text-analytics-fastapi.cognitiveservices.azure"
        ".com//text/analytics/v3.0/" +
        endpoint, headers=headers, json=document)
    return response.json()
