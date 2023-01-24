import requests
import json
import telebot

TOKEN ="5713947505:AAGiYVRjEjM-Uipmvh9G51Xr9T8an9uaI9I"
bot: telebot = telebot.TeleBot(TOKEN)

Mydict = {
    "/eur": "EUR",
    "/usd": "USD",
    "/ron": "RON",
}

class ConvertionException(Exception):
    pass
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'For new operation type : /conversion'
    bot.reply_to(message, text)

@bot.message_handler(commands=['conversion'])
def operation(message: telebot.types.Message):
    text = 'Actual currency:\n /pln_to_usd \n /pln_to_ron \n ' ,'/pln_to_eur \n /usd_to_pln \n /ron_to_pln \n /eur_to_pln'
    r1 = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
    texts1 = json.loads(r1.content)
    Rates1 = texts1.get('rates')
    EUR1 = str(Rates1[0].get('mid'))
    r2 = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/")
    texts2 = json.loads(r2.content)
    Rates2 = texts2.get('rates')
    USD1= str(Rates2[0].get('mid'))
    r3 = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/ron/")
    texts3 = json.loads(r3.content)
    Rates3 = texts3.get('rates')
    RON1= str(Rates3[0].get('mid'))

    Mydict = {
        "/eur": "",
        "/usd": "",
        "/ron": "",
    }
    Mydict['eur'] = EUR1
    Mydict['usd'] = USD1
    Mydict['ron'] = RON1
    for key in Mydict.keys():
        text = '\n'.join((text, key, '->', Mydict[key]))
    bot.reply_to(message, text)

@bot.message_handler(commands=["pln_to_usd"])
def pln_to_usd(message):
    bot.send_message(message.chat.id, "Type how many pln, you want to convert in usd")

    @bot.message_handler(content_types=["text", ])
    def plnusd(message):
        r = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/")
        texts = json.loads(r.content)
        Rates = texts.get('rates')
        USD = Rates[0].get('mid')
        amount = int(message.text)
        total = round((amount / USD), 2)
        result = f'{amount} pln зто {total} usd'
        if type(amount) == str:
            raise ConvertionException(f'did not managet to convert {amount}')

        bot.send_message(message.chat.id, result)


@bot.message_handler(commands=["pln_to_ron"])
def pln_to_ron(message):
    bot.send_message(message.chat.id, "Type how many pln, you want to convert in ron")

    @bot.message_handler(content_types=["text", ])
    def plnron(message):
        r4 = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/ron/")
        texts4 = json.loads(r4.content)
        Rates4 = texts4.get('rates')
        ron4 = Rates4[0].get('mid')
        amount4 = int(message.text)
        total4 = round((amount4 / ron4), 2)
        result4 = f'{amount4} pln зто {total4} ron'
        bot.send_message(message.chat.id, result4)
        if type(amount4) == str:
            raise ConvertionException(f'did not managet to convert {amount4}')

        bot.send_message(message.chat.id, result4)
bot.polling(none_stop=True)
