# Web scrapper for factorioprints.com/top

### Technical requirements for Project:

Python 3.8, Django 3.0, FastAPI, Selenium, RabbitMQ, Celery as a task manager

---

## Project Description

This parser project created with Django and Selenium to scrape data from https://factorioprints.com/top.
With the help of FastAPI constracted API seprarately wthin **api** folder. The project can parse and
update already saved prints in every minute according to original website.
Start project locally, go to localhost:8000 url in browser, you will see 2 main url paths,
first one is for scrapping factorioprints/top second one is for update existing prints in db every minute

deafault configuration set up to parse 10 pages, if you want to change it, you can always do it in
within parser.py file

---

## Installation Steps:

```bash
$git clone
$virtualenv -p python3.8 .venv
$source .venv/bin/activate
$pip install -r requirements.txt
```

### Running Project locally, enter to core dorectory of project and start development server

```bash
$./manage.py runserver
```


### Starting Project at Production server

```bash
$docker-compose build .
$docker-compose up
```

---

## Architecture

**admin** - contains admin panel settings and configurations,

**Views** - contains logic for accepting request data and passing to Forms and Services

**Urls** - contains URL matching patterns with Views

**Models** - contains data and object presentation logic

**Settings** - Contains Project common settings like DB, Time, etc

**Api** - contains only API presentation app implemented with FastAPI framework


## nginx

Nginx is used as a reverse proxy server, thus, all web traffic goes though it and Django is not in public network.
See more details at nginx configs at nginx/conf.d/sites-available

