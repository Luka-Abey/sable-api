### Sable Radio API

API component for Sable Radio website. Currently to store, receive, and update schedule data.

### Run locally

Clone the repo to your local machine, make sure you are in the root directory and:
Create a virtual environment for Django (venv):
```
python -m venv venv
```
Then activate the venv (Windows):
```
source venv/Scripts/activate
```
Think on Mac it is:
```
source bin/activate
```
You should see (venv) appear in the terminal. Now:
```
python manage.py migrate
```
```
python manage.py runserver
```
Django server is now running on http://localhost:8000