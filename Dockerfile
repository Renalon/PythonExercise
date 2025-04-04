# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt ./

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Указываем команду для запуска приложения через gunicorn и wsgi.py
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]