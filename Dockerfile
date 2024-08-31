# Используем базовый образ Python
FROM python:3.9-slim

# Задаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt



# Копируем весь код приложения в контейнер
COPY . .

# Указываем, какой порт будем использовать
EXPOSE 5000

# Определяем команду для запуска приложения
CMD ["python", "app.py"]
