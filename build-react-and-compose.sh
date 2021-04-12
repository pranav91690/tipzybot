#!/bin/bash
npm run build --prefix=nginx-web-server/webapps/fantasywebapp/
docker-compose up -d --build
