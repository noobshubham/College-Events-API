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
      "title": "Coding Ninjas Club - Connect to Glory",
      "start_date": "19th July 2023, 02.30 PM",
      "end_date": "19th July 2023, 03.30 PM",
      "image_poster": "https://lh4.googleusercontent.com/YyJNDz3QMCA2GwGNmA-BRTbQhDA0E6pAr1vgbKmJMesyKe5F49kQAv14TU4o7H9K3vi3I70ri3CURhz_Mc2Z06s=w1280",
      "registration_link": "https://forms.gle/CnAwoS4FhzUWtMd47"
    }
  ],
  "depart_level": [
    {
      "title": "Dept. of MCA: Guest Talk on GIT and JS",
      "start_date": "22nd July 2023, 10.30 AM",
      "end_date": "22nd July 2023, 12.00 PM",
      "image_poster": "https://lh5.googleusercontent.com/hc0KzUpffwVLmKlXZPaqAOzA5IC0Nc_ZiPph-v2ku7sOlDrxHgKKZ0j3hKfzMMdF6SWT3M9BwqDe2rDrNueEUAIFyXKw264_fJFFPtuAbqrL2pzYVmBYI9NqLEROnCuCEQ=w1280",
      "registration_link": "https://forms.gle/LYnf9zDCwEEpp5r88"
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

