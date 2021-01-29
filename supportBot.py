import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

TO_CHAT_ID = -507296089          # Не забудьте подставить нужный id!

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
    if(message.chat.id == -507296089):
       bot.send_message(message.from_user.id, '.!.')

#RUN
bot.polling(none_stop = True)


# https://habr.com/ru/post/442800/

''' 
from telebot import TeleBot


bot = TeleBot('[token]')  # Не забудьте подставить свой токен!
TO_CHAT_ID = -507296089          # Не забудьте подставить нужный id!


@bot.message_handler(content_types=['text'])
def all_messages(message):
    bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True) 
'''

'''
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
        print(message.chat.id)
'''