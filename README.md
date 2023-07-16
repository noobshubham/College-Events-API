College Events API
===================

This API retrieve event activities from the CMRIT Student Clubs Website and return them in JSON format.


Usage
---------

Send a get request to the events endpoint.

Example - https://college-event-api.onrender.com/events

For more information, [Documentation](https://college-event-api.onrender.com/docs)

Response Format
-------------------

This is how the JSON Object in response appears. 

```JSON
{
  "developer": "noobshubham",
  "student_club": [
    {
      "title": "CCA Club - Aptitude Relay - Prelims",
      "start_date": "12th July 2023, 01.00 PM",
      "end_date": "12th July 2023, 04.00 PM",
      "image_poster": "https://lh6.googleusercontent.com/ey5Zmf56T1pi3b7Oq52albn08KOfEqa3VMU7oAEVnXkV5_5uMZZLIuV4R0qj35euGUCajBtvm8xOS20aXbulSLggK_Kys4-n9blraU95mc5uLqgquDQn415W9vYW5Qn0Cw=w1280",
      "registration_link": "https://forms.gle/RgWEtyF12cfhL2ed8"
    }
  ],
  "depart_level": [
    {
      "title": "IIC - Dept. of CSE: Workshop on Prototype Validation - Achieving Value Proposition Fit & Business Fit",
      "start_date": "20th July 2023, 02.00 PM",
      "end_date": "20th July 2023, 03.00 PM",
      "image_poster": "https://lh4.googleusercontent.com/8EtmVImFMwZuiY6Z0OHpNXC7zmaRrewFlb1GQsUllVQz7JWQF5uerhmbmoi9qPwJNAVJFke9SAskx8u04dEGBmY=w1280",
      "registration_link": null
    }
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

