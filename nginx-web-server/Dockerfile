FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
ADD webapps/fantasywebapp/build /usr/share/nginx/html/
# ADD webapps/flowrate/build /usr/share/nginx/html/flowrate
RUN rm /etc/nginx/conf.d/default.conf