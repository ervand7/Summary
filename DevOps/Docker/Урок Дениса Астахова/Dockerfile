#---------------------------------------------------------------------------
# Dockefile to build Docker Image of Apache WebServer running on Ubuntu
#
# Made by Denis Astahov ADV-IT  13-March-2019
#---------------------------------------------------------------------------

FROM ubuntu:16.04
# "ubuntu:16.04" - это название нашего образа

# далее запускаем линуксовые команды на этом образе: обновить и скачать
RUN apt-get -y update
# подробнее: https://qastack.ru/ubuntu/222348/what-does-sudo-apt-get-update-do
# -y - это разрешение подсказок
RUN apt-get -y install apache2

RUN echo 'Hello World from Docker!' > /var/www/html/index.html
# созраняем echo в файл /var/www/html/index.html

CMD ["/usr/sbin/apache2ctl", "-D","FOREGROUND"]
# запускаем сервер apache2ctl на бэкграунде
EXPOSE 80
# говорим, что используем 80 порт
