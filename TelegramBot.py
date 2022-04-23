import telebot ; import json ; import time

bot = telebot.TeleBot("TOKEN",parse_mode='HTML')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """
    سلام!
    اگه می‌خوای دلار بخری بخری: /USD
    اگه می‌خوای رمز ارز تتر تهیه کنی: /USDT
    :>
    """)


json_file = open('json_data.json')
data = json.load(json_file)
        

@bot.message_handler(commands=['USD'])
def send_price(message):

	bot.reply_to(message, """
    در حال حاضر این فروشگاه‌ها دلار می‌فروشن:

    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>

    
    اگه می‌خوای رمز ارز تتر تهیه کنی: /USDT

    """

    %(data['USD']['Shop_1']['Name'],data['USD']['Shop_1']['Buy_Price'],
    data['USD']['Shop_1']['Description'],data['USD']['Shop_1']['Link'],
    data['USD']['Shop_2']['Name'],data['USD']['Shop_2']['Buy_Price'],
    data['USD']['Shop_2']['Description'],data['USD']['Shop_2']['Link'],
    data['USD']['Shop_3']['Name'],data['USD']['Shop_3']['Buy_Price'],
    data['USD']['Shop_3']['Description'],data['USD']['Shop_3']['Link'],
    data['USD']['Shop_4']['Name'],data['USD']['Shop_4']['Buy_Price'],
    data['USD']['Shop_4']['Description'],data['USD']['Shop_4']['Link'],

    )

    )


@bot.message_handler(commands=['USDT'])
def send_price(message):

	bot.reply_to(message, """
    در حال حاضر این فروشگاه‌ها دلار می‌فروشن:

    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>
    %s - %s - %s - <a href="%s">خرید</a>

    
    اگه می‌خوای دلار بخری بخری: /USD

    """

    %(data['USDT']['Shop_1']['Name'],data['USDT']['Shop_1']['Buy_Price'],
    data['USDT']['Shop_1']['Description'],data['USD']['Shop_1']['Link'],
    data['USDT']['Shop_2']['Name'],data['USDT']['Shop_2']['Buy_Price'],
    data['USDT']['Shop_2']['Description'],data['USD']['Shop_2']['Link'],
    data['USDT']['Shop_3']['Name'],data['USDT']['Shop_3']['Buy_Price'],
    data['USDT']['Shop_3']['Description'],data['USD']['Shop_3']['Link'],
    data['USDT']['Shop_4']['Name'],data['USDT']['Shop_4']['Buy_Price'],
    data['USDT']['Shop_4']['Description'],data['USDT']['Shop_4']['Link'],

    )

    )

bot.infinity_polling()

startTime = time.time()

#reloading json file
while True:
    if time.time()-startTime >= 6000:     #after one hour
        startTime = time.time()
        json_file = open('json_data.json')
        data = json.load(json_file)
