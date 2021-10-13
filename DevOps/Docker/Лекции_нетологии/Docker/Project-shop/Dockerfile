FROM python:3.8
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install -r requirements.txt
WORKDIR project_shop

CMD ["python", "./manage.py", "runserver", "0.0.0.0:7777"]