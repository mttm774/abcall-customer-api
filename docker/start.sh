#!/bin/sh
# Ensure the /run/nginx directory exists
mkdir -p /run/nginx

# Start Gunicorn (your Python app)
make docker-gunicorn PORT=8000 &

# Start Nginx
nginx -g 'daemon off;'