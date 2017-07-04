import config
import requests
import telebot

from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Лампа 1', 'Лампа 2', 'Выкл']])
    msg = bot.send_message(m.chat.id, 'Выберите лампу?',
        reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
	if m.text == 'Лампа 1':
		bot.send_message(m.chat.id, '*Лампа 1* триггер', parse_mode='Markdown')
		requests.post('http://192.168.1.177', data={'r1':'$0'})
	elif m.text == 'Лампа 2':
		bot.send_message(m.chat.id, '*Лампа 2* триггер', parse_mode='Markdown')
		requests.post('http://192.168.1.177', data={'r2':'$0'})
	elif m.text == 'Выкл':
		bot.send_message(m.chat.id, '*Выключение*', parse_mode='Markdown')
		requests.post('http://192.168.1.177', json={'r1':'$0'})
	start(m)

#if __name__ == '__main__':
#	bot.polling(none_stop=True)
bot.polling()