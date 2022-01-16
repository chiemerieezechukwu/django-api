# Cars API
[![Django CI](https://github.com/chiemerieezechukwu/django-api/actions/workflows/django-workflow.yml/badge.svg?branch=master)](https://github.com/chiemerieezechukwu/django-api/actions/workflows/django-workflow.yml)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/chiemerieezechukwu/a1817190b63b0cd8f551cb3ec2ab6524/raw/django-api_master_coverage.json)

## Getting started quickly
Clone this repository and rename the `.env.example` in the root of the project to `.env`

Install requirements with the `requirements.txt` file
```
$ pip install -r requirements.txt
```

## Docker Compose
make sure you're at the root of the project then run
```
$ docker-compose up
```
It will perform database migrations and the api will be served by gunicorn on `http://localhost:8000`

## Running on local machine
If you prefer not to use docker
```
$ python manage.py migrate && python manage.py runserver
```

## Populating the database
A django management command `python manage.py data_from_csv <csv_file>` exists to populate the database automatedly.

Usage example
```
$ python manage.py data_from_csv cars.csv
```
It will add car entries to the database utilizing the csv file `cars.csv` already present at the root of this project

## Running tests inside Docker
With the containers still running, run the following command to execute all test cases
```
$ docker exec -it cars-api python -m pytest
```

## Running tests locally
```
$ pytest
```
