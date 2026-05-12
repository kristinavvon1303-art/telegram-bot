import telebot
import time

TOKEN = "8464604971:AAEGOCqovQFXj4mO0E7fFK1cFLdEhM32Z6I"
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
        "Из какого я канала? Дай-ка вспомнить... А, точно! Я из... Аэ.. подожди-ка... А, всё, я вспомнила!\n\n"
        "Я из @NereyasUnderwaterWorld !\n\n"
        "Наверное, этот канал был создан в честь меня, ведь я отлично выполняла свою работу. Точнее, я надеюсь на это…",
        3
    )


# 3️⃣ команда /asknereyaabouther
@bot.message_handler(commands=['asknereyaabouther'])
def about(message):
    typing(
        message.chat.id,
        "Хочешь узнать обо мне побольше? Тогда давай поговорим сначала о моих друзьях! Я очень их ценю и люблю. "
        "Моя лучшая подруга это Джи джи, она часто подшучивает надо мной и говорит то, что медузы вкусные, хоть я и не особо понимаю о чём она. "
        "А ещё Браша, с ней весело проводить время и Кокоа, она мне часто помогает и выручает. Очень ценю их!\n\n"
