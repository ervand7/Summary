# Web chat

[![web-chat](https://github.com/artrey/web-chat/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/artrey/web-chat/actions/workflows/ci.yml)

[![Python](https://img.shields.io/badge/-Python-ffde57?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-092e20?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-c9510c?style=flat-square&logo=drf)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-bbeedd?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-008272?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-f5f5f5?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Heroku](https://img.shields.io/badge/-Heroku-6762a6?style=flat-square&logo=Heroku)](https://heroku.com/)
[![Docker](https://img.shields.io/badge/Docker-white.svg)](https://docker.com/)


## Usage

### Preparing phase

1. Make `.env` with desired variables (optional)

2. Run the commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Developing

```bash
pip install -r requirements-dev.txt
```
