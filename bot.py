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


# 3️⃣ получение вопроса
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


# 4️⃣ ответ админа (через reply)
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


# 5️⃣ fallback
@bot.message_handler(func=lambda message: True)
def fallback(message):
    if message.chat.id not in ADMINS:
        typing(message.chat.id, "Используй /asknereya чтобы задать вопрос!", 1.5)


bot.infinity_polling()
