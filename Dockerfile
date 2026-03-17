# Используем официальный образ Python 3.11
FROM python:3.11

# Устанавливаем зависимости для Playwright / Chromium
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
    libgdk-pixbuf-xlib-2.0-0 \
    libxrender1 \
    libfontconfig1 \
    libfreetype6 \
    libdbus-1-3 \
    curl \
    wget \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория приложения
WORKDIR /app

# Копируем весь код проекта внутрь контейнера
COPY . .

# Обновляем pip и устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем браузеры для Playwright
RUN playwright install

# Команда запуска автопостинга
CMD ["python", "main.py"]
