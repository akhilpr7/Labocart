FROM python:3.8

ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY . .

RUN pip3 install -r requirements.txt

CMD python manage.py runserver 0:8000
