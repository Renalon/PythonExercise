#!/bin/bash

# Запуск Gunicorn с правильным портом
gunicorn --bind 0.0.0.0:$PORT wsgi:app &  
APP_PID=$!

# Ждем, пока сервер стартует
sleep 25  

echo "Start client"
python3 client.py
APP_CODE=$?

# Даем серверу чуть-чуть поработать перед выключением
sleep 5  

echo "Stopping Gunicorn (PID: $APP_PID)"
kill -TERM $APP_PID

echo "App exit code: $APP_CODE"
exit $APP_CODE