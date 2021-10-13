FROM nginx

# удалим дефолтный конфиг и скопируем туда наш конфиг
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d