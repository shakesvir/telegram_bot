import telebot

bot = telebot.TeleBot('6573598701:AAH-4NR2zxmc7wNeOLrKBc3Dn-svTw_5JDE')

@bot.message_handler()

def main(message):
     bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)