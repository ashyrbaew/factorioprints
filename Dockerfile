FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc netcat && apt-get install -y gettext

RUN mkdir /app -p
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app/
#EXPOSE 8000

#CMD ["python", "manage.py", "runserver"]
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]