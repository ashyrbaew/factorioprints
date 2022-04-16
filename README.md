# Web scrapper for factorioprints.com/top

Technical requirements for Project:

Language: Python 3.8

Framework: Django 3.0

API Framework: FastAPI

Scrapy software: Selenium

Message broker: RabbitMQ

Task Scheduler: Celery

---

## Installation Steps:

```bash
git clone
virtualenv -p python3.8 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Project locally, enter to core dorectory of project and start development server

```bash
./manage.py runserver
```


## Starting Project at Production server

### Starting server

```bash
docker-compose build .
docker-compose up
```


## Architecture

**admin** - contains admin panel settings and configurations,

**Views** - contains logic for accepting request data and passing to Forms and Services

**Urls** - contains URL matching patterns with Views

**Models** - contains data and object presentation logic

**Settings** - Contains Project common settings like DB, Time, etc

**Api** - contains only API presentation app implemented with FastAPI framework


## **Project Workflow Description**

This parser project build with Django and Selenium to scrape data from and used FastAPI for API constraction
Start project locally, go to localhost:8000 url in browser, you will see 2 url paths

first one is for scrapping factorioprints/top second one is for update existing prints in db every minute
so, if some prints dissapears from original website id will update our databse accordingly
to view current prinst just start FastAPI project which is located in API directory and check url locally


## nginx

Nginx is used as a reverse proxy server, thus, all web traffic goes though it and Django is not in public network.
See more details at nginx configs at nginx/conf.d/sites-available

