# Coded by Shubham on 15 July 2023

from fastapi import FastAPI
import student_club
import depart_level

app = FastAPI()

eventsDictionary = {
    'developer': 'noobshubham',
    'student_club': [],
    'depart_level': [],
    'success': True
}

@app.get('/')
async def home():
    return "The CMRIT Student Club API is UP! Maintained and Developed by SHUBHAM from MCA."

@app.get("/events")
async def get_events():
    eventsDictionary['student_club'] = student_club.events()
    eventsDictionary['depart_level'] = depart_level.events()
    return eventsDictionary

