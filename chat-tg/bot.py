import telebot

bot = telebot.TeleBot("7553579655:AAFJcmQYsEgJu9mhDRLrOmb56tazwCoH77g")

@bot.message_handler()
def message_handler(msg):
	try:
		if msg.chat.id == -1002355287793:
			print(f"@{msg.from_user.username}: {msg.text}")
			text = input()
			bot.send_message(msg.chat.id, text)
	except Exception as e:
		bot.send_message(msg.chat.id, e)

bot.polling()
