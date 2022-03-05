# Web scrapper for factorioprints.com/top

Tech stack used in Project:
Language: Python 3.8
Framework: Django 3.0
API Framework: FastAPI
Scrapy software: Selenium
Message broker: RabbitMQ
Task Scheduler: Celery

## Installation Steps:

```bash
git clone
virtualenv -p python3.8 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Running Project locally
## Starting development server

```bash
./manage.py runserver --settings estekg.settings.dev
```

#Starting Project at Production server
## Starting server

```bash
docker-compose build .
docker-compose up
```

## Architecture

**Views** - contain logic for accepting request data and passing to Forms and Services

**Services** - contain business logic only

**Models** - contain data and object presentation logic

**Forms** - contain logic for validating if request data is clean, exists and of proper format and shape.

Read more about Services layer to get more understanding. Read more about Single Responsibility Principle.


## nginx

Nginx is used as a reverse proxy server, thus, all web traffic goes though it and Django is not in public network.
Since every subdomain uses different landing pages, the solution is to dispatch traffic using Host request header.
See more details at nginx configs at nginx/conf.d/sites-available

