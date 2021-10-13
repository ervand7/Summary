FROM python:3.8
COPY ./app /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
