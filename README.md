### Sable Radio API

API component for Sable Radio website. Currently to store, receive, and update schedule data.

Available endpoint URLs:
| URL | Accessed Data  | Notes |
--- | --- | ---
| /api/schedule | returns all shows in database | if schedule is implemented, will need to match this on current week |
| /api/schedule/currentshow | returns show which matches time.now | |
| /api/residents | returns all residents | |
| /api/residents/\<id> | returns resident with matching id | |
| /api/residents/search/<query_string> | returns residents matching with query | matches `name` and `description`|

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