FROM python:3

WORKDIR /usr/src/app

COPY project_shop .
COPY entrypoint.sh /usr/src

RUN pip install -r requirements.txt

RUN chmod +x /usr/src/entrypoint.sh

ENTRYPOINT ["/usr/src/entrypoint.sh"]