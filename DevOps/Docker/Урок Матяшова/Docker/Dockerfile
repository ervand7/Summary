FROM python:3.8

RUN mkdir -p /usr/src/app2
WORKDIR /usr/src/app2

# Следующая команда актуальна для БД. Информация, которая хрантся по этому пути, хранится в docker volume.
# БД именно здесь будет сохранять какую-то информацию. При остановке контейнера данные не исчезают. Мы просто можем
# привязать этот volume к другому контейнеру
COPY . /usr/src/app2
# Следующая команда только для app2. Это для автоматической установки reqirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# следующая команда декларирует, что мы пробрасываем порт 8080
EXPOSE 8080

# следующая команда прописывает переменную окружения. В данном случае, чтобы у нас правильно отображался часовой пояс
#ENV TZ Europe/Moscow

CMD ["python", "app2.py"]

