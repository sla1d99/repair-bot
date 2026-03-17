# Используем официальную версию Playwright Python, совпадающую с Playwright 1.58.0
FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy

# Рабочая директория
WORKDIR /app

# Копируем весь код проекта
COPY . .

# Обновляем pip и ставим зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установка браузеров Playwright (Chromium, Firefox, WebKit)
RUN playwright install

# Команда запуска вашего автопостинга
CMD ["python", "main.py"]
