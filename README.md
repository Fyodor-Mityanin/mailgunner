# MailGunner project

This is a test project for work

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Docker v20.10.2 or newer
```

### Installing

Clone repository to your pc and install requirements to you venv and run Docker-Compose

```
docker-compose up
```

Then you need to be sure that container with Redis is running

```
docker container ls
```
You need to create .env file and fill it with your data. Watch .env.example file in root directory, it's example.

Now you need to run Celery

```
celery -A mailgunner worker -l INFO --pool=solo
```

Now you need to make migrations

```
python manage.py makemigrations
python manage.py migrate
```

and create superuser

```
python manage.py createsuperuser
```

So now you can start MailGunner

```
python manage.py runserver
```

You can fill DB with E-Mails from localhost/admin or localhost/emails page



## Built With

* [Django 3.2](https://docs.djangoproject.com/en/3.2/) - The web framework used
* [Docker 20.10.2](https://www.docker.com/) - Package software used
* [Celery 5.1.2](https://docs.celeryproject.org/en/stable/) - Distributed Task Queue
* [Redis 6.2](https://redis.io/) - Message broker


## Authors

* **Fedor Mityanin** - [Fyodor-Mityanin](https://github.com/Fyodor-Mityanin)
