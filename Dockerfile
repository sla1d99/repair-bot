FROM python:3.11

WORKDIR /app
COPY . .

# Установка всех зависимостей для Playwright / Chromium
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
    libvulkan1 \
    libgtk-4-1 \
    libflite1 \
    libflite-usenglish-1.0 \
    libopus0 \
    libgstreamer-1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libgstvideo-1.0-0 \
    libgstapp-1.0-0 \
    libgstpbutils-1.0-0 \
    libgsttag-1.0-0 \
    libgstcodecparsers-1.0-0 \
    libgstallocators-1.0-0 \
    libgstfft-1.0-0 \
    libgraphene-1.0-0 \
    libenchant-2-2 \
    libsecret-1-0 \
    libhyphen0 \
    libwoff2dec1 \
    libx264-163 \
    curl \
    wget \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Python зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Установка браузеров Playwright
RUN playwright install

CMD ["python", "main.py"]
