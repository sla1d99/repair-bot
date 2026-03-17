from playwright.sync_api import sync_playwright
import time
import os
import schedule
import random
from openai import OpenAI

os.system("playwright install")

client = OpenAI()

EMAIL = "rrruuupppp"
PASSWORD = "SL@1D5462429"

# =========================
# 🤖 AI ПОСТЫ
# =========================
def generate_post():
    topics = ["психология", "деньги", "привычки", "лайфхаки"]

    prompt = f"""
    Напиши вирусный пост для Threads.

    Тема: {random.choice(topics)}

    Коротко, цепляюще:
    - 1 сильный заход
    - 2-4 пункта
    - в конце вопрос или "напиши +"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    return response.choices[0].message.content


# =========================
# 🤖 AI ОТВЕТЫ
# =========================
def generate_reply_ai(user_text):
    prompt = f"""
    Человек написал: {user_text}

    Ответь коротко, по-дружески, как блогер.
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

        page.fill('input[name="username"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)
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

        page.fill('input[name="username"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')

        time.sleep(10)

        page.goto("https://www.threads.net/activity")
        time.sleep(5)

        messages = page.query_selector_all("div[role='button']")

        for msg in messages[:5]:
            try:
                text = msg.inner_text().lower()

                if "+" in text:
                    reply = "Сейчас скину ещё один лайфхак 👇"
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
# 🔁 ОСНОВНАЯ ЛОГИКА
# =========================
def run():
    post = generate_post()
    print("POST:", post)
    post_to_threads(post)


# 🔥 тест сразу
run()

# ⏰ расписание
schedule.every().day.at("10:00").do(run)
schedule.every().day.at("18:00").do(run)
schedule.every(10).minutes.do(check_messages_and_reply)

print("🤖 Бот запущен...")

while True:
    schedule.run_pending()
    time.sleep(60)
