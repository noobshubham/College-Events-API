# Coded by Shubham on 15 July 2023

import requests
from bs4 import BeautifulSoup

def events():
  """Scrapes the events from the CMRIT student clubs website."""
  url = "https://sites.google.com/cmrit.ac.in/cmritstudentclubs/events"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  events = []
  for event in soup.find_all("section", class_="yaqOZd qeLZfd"):
    title = event.find("p", class_="zfr3Q CDt4Ke").text
    image_poster = event.find("img")["src"] 
    registration_link = event.find("a", class_="XqQF9c")
    if registration_link and registration_link["href"]:
        registration_link = registration_link["href"]
    else:
        registration_link = None

    events.append({
        "title": title,
        # "date": start_date_and_time,
        "image_poster": image_poster,
        "registration_link": registration_link,
    })

  return events

if __name__ == "__main__":
  events = events()
  for event in events:
    print(event)
