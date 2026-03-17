# Базовый образ с полной поддержкой зависимостей GUI
FROM python:3.11

# Установка зависимостей для Playwright / Chromium
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcb-shm0 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libcairo2 \
    libatk1.0-0 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libxrender1 \
    libfontconfig1 \
    libfreetype6 \
    libdbus-1-3 \
    curl \
    wget \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app
COPY . .

# Обновляем pip и ставим зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установка браузеров для Playwright
RUN playwright install

# Команда запуска вашего скрипта
CMD ["python", "main.py"]
