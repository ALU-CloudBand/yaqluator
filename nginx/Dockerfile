FROM nginx:stable-alpine

RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.orig

COPY nginx.conf /etc/nginx/nginx.conf
COPY yaqluator.conf /etc/nginx/conf.d/yaqluator.conf
