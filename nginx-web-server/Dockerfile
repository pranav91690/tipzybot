FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
ADD webapps/fantasywebapp/build /usr/share/nginx/html/
RUN rm /etc/nginx/conf.d/default.conf