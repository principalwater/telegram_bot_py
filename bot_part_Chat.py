import telebot
import apiai, json
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'small-talk-itgl-af22f625*****.json'

DIALOGFLOW_PROJECT_ID = 'small-talk-itgl'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'

bot = telebot.TeleBot("5416605580:AA*****-fo_wKbx*****_ZwO96GD***No")

# Start command handling module
@bot.message_handler(commands=['start'])
def send_start(message):
	bot.reply_to(message, "Привет, напиши мне что-нибудь хорошее :)")

# Text messages handling module
@bot.message_handler(content_types=['text'])
def send_msg(message):
    text_to_be_analyzed = message.text
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        result = response.query_result.fulfillment_text
    except InvalidArgument:
        raise
    bot.reply_to(message, result)
# Running the bot from now on
bot.infinity_polling()