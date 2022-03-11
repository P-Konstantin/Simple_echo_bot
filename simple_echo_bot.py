import telebot


# Создаем экземпляр бота
bot = telebot.TeleBot('token')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь ')


# Получение сообщений от пользователя
@bot.message_handler(content_types=['text'])
def handler_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)

