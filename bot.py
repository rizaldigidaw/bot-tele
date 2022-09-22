import telebot

bot = telebot.TeleBot("1559560627:AAElkke4Go3cCuY06tPa8OpBR3fhD03hUqY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 if message.startswith("hi"):
     bot.reply_to(message,"Hallo")
bot.infinity_polling()
