FROM python:3.8

COPY ./ad_api_on_flask /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["gunicorn", "app:app"]
