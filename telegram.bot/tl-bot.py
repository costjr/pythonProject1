import telebot
import random
from telebot import types
bot = telebot.TeleBot("5713947505:AAGiYVRjEjM-Uipmvh9G51Xr9T8an9uaI9I")
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😀 Random Number")
    item2 = types.KeyboardButton("😎 How are you?")
    item3 = types.KeyboardButton("Phone")
    item4 = types.KeyboardButton("Car")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,"hola",parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def dialog(message):
    if message.chat.type == 'private':
        if message.text == '😀 Random Number':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "😎 How are you?":

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('Good', callback_data='good')
            item2 = types.InlineKeyboardButton("Bad", callback_data='bad')
            item3 = types.InlineKeyboardButton("IDK", callback_data='idk')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Nice, you?", reply_markup=markup)
        elif message.text == 'Phone':
            from request import scrape_data
            phones = scrape_data()
            bot.send_message(message.chat.id, random.choice(phones))
        elif message.text == 'Car':
            from request import scrape_car
            cars = scrape_car()
            bot.send_message(message.chat.id, random.choice(cars))
        else:
            bot.send_message(message.chat.id, "I don't have an answer for that")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "Nice")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "Why?")
            elif call.data == 'idk':
                bot.send_message(call.message.chat.id, "Ok")

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="How are you",
                                  reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=True,
                                      text="Test Allert")

    except Exception as e:
           print(repr(e))

bot.polling(none_stop=True)