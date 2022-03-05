#!/bin/sh

    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done
    echo "PostgreSQL started"

    echo "Migrate the Database at startup of project"
    python manage.py migrate --settings ${DJANGO_SETTINGS_MODULE} --noinput

    echo "Update translation fields"
    python manage.py update_translation_fields --settings ${DJANGO_SETTINGS_MODULE}

    echo "Collect staticfiles at startup of project"
    python manage.py collectstatic --settings ${DJANGO_SETTINGS_MODULE} --noinput

    echo "generate html translations"
    python manage.py compilemessages --settings ${DJANGO_SETTINGS_MODULE}


    echo "RUNNING DEV SERVER DJANGO__________"
    python manage.py runserver 0.0.0.0:8000

#    echo "Running gunicorn======================"
#    gunicorn factorioprints.wsgi:application --bind 0.0.0.0:8000 --config='/app/factorioprints/gunicorn.py' --workers=3
