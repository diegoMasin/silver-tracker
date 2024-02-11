![Alt text](https://raw.githubusercontent.com/diegoMasin/landing-maximumtech/master/assets/img/new-logo-mt-01.png)
<br><br>

# Silver Tracker

###### Basic control of the sale of jewelry and semi-jewelry.

## Requirements

- Python 3.10.11

## Install Project

```
- clone repository
- cd <project-folder>
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt
- python contrib/env_gen.py
- change .env file mainly if be use another database
-- not forget create database, change settings.py and add lib in requirements.txt if needed
- python manage.py migrate
- python manage.py createsuperuser --username="admin" --email=""
- python manage.py runserver
```

## More info

```
- Main goals is to use django-admin
- Have DRF for future possibility to use this project as only backend
```
