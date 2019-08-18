FROM python:3

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev python3-gdal && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY docker_requirements.txt /code/
RUN pip install -r docker_requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
