College Events API
===================

Usage
---------

Send a get request to the events endpoint.

Example - https://college-event-api.onrender.com/events

Response Format
-------------------

This is how the JSON Object in response appears. 

```JSON
{
  "developer": "noobshubham",
  "data": [
    {
      "title": "CCA Club - Aptitude Relay - Prelims",
      "image_poster": "https://lh4.googleusercontent.com/oMVRtcwo6s2gUegFFm69n3djda1c63bh2s27A7WZliHlX5Nf8T2rq98BxyinpfdkUHmQnaGbfsAT7M82uNXyZNgZpIsQrUq8szDB-EBgVSF5U1uL9Xu4gR9IIL38L3VAGQ=w1280",
      "registration_link": "https://forms.gle/RgWEtyF12cfhL2ed8"
    },
    {
      "title": "FEEE Club - Poster Designing",
      "image_poster": "https://lh3.googleusercontent.com/DucAjz0hS1zE0eWM67bIfx8OdmvWne-wgfzi4psJIK99cMpCiETTrhvhRo-iijo0HP5qJf96lqEkqjWGWJOJ4yk=w1280",
      "registration_link": "https://forms.gle/RjhQxkDYekZtkXs47"
    },
  ],
  "success": true
}
```

Setup
------

Install all dependencies listed in _requirements.txt_ file.

1. To install all dependencies run

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server

   ```bash
   python -m uvicorn app:app --reload
   ```

