FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY vue.global.prod.js /usr/share/nginx/html/vue.global.prod.js

EXPOSE 80
