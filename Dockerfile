# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем необходимые библиотеки для работы OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем весь код приложения в контейнер
COPY . /app

# Указываем команду для запуска приложения
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]