import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add('Технічна підтримка користувачів')
keyboard1.add('Інформація про оплату')
keyboard1.row('Українська', 'English', 'Русский')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Оберіть дію:', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'технічна підтримка користувачів':
        bot.send_message(message.chat.id, 'supportInfo')
    if message.text.lower() == 'інформація про оплату':
        bot.send_message(message.chat.id, 'paymentInfo')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

#RUN
bot.polling(none_stop = True)