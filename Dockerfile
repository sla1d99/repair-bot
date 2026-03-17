# Используем официальный образ Playwright с Python
FROM mcr.microsoft.com/playwright/python:latest

# Рабочая директория
WORKDIR /app

# Копируем весь код проекта
COPY . .

# Обновляем pip и ставим зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD запускает ваш скрипт автопостинга
CMD ["python", "main.py"]
