import telebot
import time

TOKEN = "8464604971:AAFcG6TDdDRom7F50hPZuxeuXtbe-wwo2UU"
ADMINS = [5685078094]

bot = telebot.TeleBot(TOKEN)

waiting_users = {}

# функция "печатает..."
def typing(chat_id, text, delay=2):
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    bot.send_message(chat_id, text)


# 1️⃣ команда /asknereya
@bot.message_handler(commands=['asknereya'])
def ask_start(message):
    typing(
        message.chat.id,
        "П-привет!! Тебе надо что-то спросить у меня? Задавай, я отвечу на любой вопрос!"
    )
    waiting_users[message.chat.id] = True


# 2️⃣ команда /askchannel
@bot.message_handler(commands=['askchannel'])
def channel(message):
    typing(
        message.chat.id,
        "Из какого я канала? Дай-ка вспомнить... А, точно! Я из @NereyasUnderwaterWorld !",
        3
    )


# 3️⃣ команда /asknereyaabouther
@bot.message_handler(commands=['asknereyaabouther'])
def about(message):
    typing(
        message.chat.id,
        (
            "Хочешь узнать обо мне побольше? Тогда давай поговорим сначала о моих друзьях! "
            "Я очень их ценю и люблю. Моя лучшая подруга Джи джи, она часто подшучивает надо мной. "
            "А ещё Браша, с ней весело проводить время, и Кокоа, она мне часто помогает.\n\n"

            "Насчёт других… Тиша меня не очень любит, потому что я иногда её раздражаю водой. "
            "А Финн однажды кинул в меня рыбу, с тех пор я его избегаю...\n\n"

            "Мой MBTI — INFP.\n\n"

            "Я плохо понимаю намёки, особенно романтические.\n\n"

            "Интересный факт: в моей комнате всегда вода на полу, мне так комфортнее."
        ),
        4
    )


# 4️⃣ получение вопроса
@bot.message_handler(func=lambda message: message.chat.id in waiting_users)
def get_question(message):
    user_id = message.chat.id

    if message.text.startswith("/"):
        return

    for admin in ADMINS:
        bot.send_message(
            admin,
            f"ID: {user_id}\nВопрос:\n{message.text}"
        )

    del waiting_users[user_id]


# 5️⃣ ответ админа (через reply)
@bot.message_handler(func=lambda message: message.chat.id in ADMINS)
def reply(message):
    if message.reply_to_message:
        try:
            user_id = int(
                message.reply_to_message.text.split("\n")[0].replace("ID: ", "")
            )
            typing(user_id, message.text, 2)
        except:
            pass


# 6️⃣ fallback
@bot.message_handler(func=lambda message: True)
def fallback(message):
    if message.chat.id not in ADMINS:
        typing(message.chat.id, "Используй /asknereya чтобы задать вопрос!", 1.5)


bot.infinity_polling()
