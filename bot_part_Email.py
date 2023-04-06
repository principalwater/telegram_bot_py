import telebot
import datetime
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import apiai, json

# TOKEN
TOKEN = '5400441336:AAEW***9S7Q0J4K3T0y0ECf5Kqf*****'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    msg = bot.send_message(message.chat.id,
                           text='Welcome!',
                           reply_markup=keyboard)

#@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['send_msg'])
def send_email(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        port = 465  # For SSL
        smtp_server = "smtp.yandex.ru"
        sender_email = "kuzmi-vl@yandex.ru"  # Enter your address
        receiver_email = ['*****@gmail.com','kuzmin.vv@yahoo.com']  # Enter receiver address
        password = "yourAccuratelySuggestedPass"
        message1 = message.text

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message1)


        bot.reply_to(message, "Message send")
    except Exception:
        bot.reply_to(message, "ERROR")

bot.polling(none_stop=True, interval=0)