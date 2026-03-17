from playwright.sync_api import sync_playwright
import time
from openai import OpenAI

client = OpenAI()
import os
import schedule
import random

# 🔐 ДАННЫЕ (вставь свои)
EMAIL = "rrruuupppp"
PASSWORD = "SL@1D5462429"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# =========================
# 🤖 AI ГЕНЕРАЦИЯ ПОСТОВ
# =========================

def generate_post():
    topics = [
        "психология",
        "привычки",
        "деньги",
        "мотивация",
        "жизненные лайфхаки"
    ]

    topic = random.choice(topics)

    prompt = f"""
    Напиши вирусный пост для Threads.

    Тема: {topic}

    Условия:
    - коротко и цепляюще
    - как будто пишет человек
    - 1 сильный заход
    - 2-4 пункта
    - в конце вовлечение (вопрос или "напиши +")

    Без воды.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=180
    )

    return response.choices[0].message.content.strip()


# =========================
# 🧠 AI ОТВЕТЫ
# =========================

def generate_reply_ai(user_text):
    prompt = f"""
    Человек написал: "{user_text}"

    Ответь как блогер с лайфхаками.
    Коротко, живо, по-дружески.
    Продолжи диалог.
    """

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

return response.choices[0].message.content


# =========================
# 🚀 ПОСТИНГ
# =========================

def post_to_threads(text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.threads.net/login")
        time.sleep(5)

        page.fill('input[name="rrruuupppp"]', EMAIL)
        page.fill('input[name="SL@1D5462429"]', PASSWORD)
        page.click('button[type="submit"]')

        time.sleep(10)

        page.goto("https://www.threads.net/")
        time.sleep(5)

        page.click("text=Start a thread")
        time.sleep(3)

        page.fill("textarea", text)
        page.click("text=Post")

        time.sleep(5)
        browser.close()


# =========================
# 💬 АВТООТВЕТЫ
# =========================

def check_messages_and_reply():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.threads.net/login")
        time.sleep(5)

        page.fill('input[name="rrruuupppp"]', EMAIL)
        page.fill('input[name="SL@1D5462429"]', PASSWORD)
        page.click('button[type="submit"]')

        time.sleep(10)

        page.goto("https://www.threads.net/activity")
        time.sleep(5)

        messages = page.query_selector_all("div[role='button']")

        for msg in messages[:5]:
            try:
                text = msg.inner_text().lower()

                if "+" in text:
                    reply = "Сейчас скину ещё один мощный лайфхак 👇"
                elif "как" in text or "почему" in text:
                    reply = generate_reply_ai(text)
                else:
                    reply = generate_reply_ai(text)

                msg.click()
                time.sleep(3)

                page.fill("textarea", reply)
                page.click("text=Reply")

                time.sleep(2)

            except:
                continue

        browser.close()


# =========================
# 🔁 ОСНОВНАЯ ФУНКЦИЯ
# =========================

def run():
    post = generate_post()
    print("POST:", post)
    post_to_threads(post)


# =========================
# ⏰ РАСПИСАНИЕ
# =========================

schedule.every().day.at("10:00").do(run)
schedule.every().day.at("19:30").do(run)

schedule.every(10).minutes.do(check_messages_and_reply)

print("🤖 Бот запущен...")

run()

while True:
    schedule.run_pending()
    time.sleep(60)
