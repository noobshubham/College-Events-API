# Coded by Shubham on 15 July 2023

from fastapi import FastAPI
import events

app = FastAPI()

@app.get('/')
async def home():
    return 'The CMRIT Student Club Activities API is UP!<br><br>Maintained and Developed by <a href="https://github.com/noobshubham">SHUBHAM</a>'

@app.get("/events")
async def get_events():
    eventsDictionary = {
        'developer': 'noobshubham',
        'data': [],
        'success': True
    }
    eventsDictionary['data'] = events.events()
    return eventsDictionary
