import telebot
import apiai, json
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from stackapi import StackAPI

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'small-talk-itgl-a*****.json'

DIALOGFLOW_PROJECT_ID = 'small-talk-itgl'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'

bot = telebot.TeleBot("541660***:AAF*********6GDGqEJmlNo")

# Start command handling module
@bot.message_handler(commands=['start'])
def send_start(message):
	bot.reply_to(message, "Привет, напиши мне что-нибудь хорошее :)")

# StackOverFlow integration handler
@bot.message_handler(commands=['stack'])
def stack_find(message):
    try:
        answers_hash = {}
        # Example ids
        #ids = input()
        ids = message.text
        ids = ids[7:]
        api_filter = '!9f*CwGV65'

        # Call the API
        SITE = StackAPI('stackoverflow')
        answers = SITE.fetch('questions/{ids}/answers',
                     ids = ids,
                     sort = 'votes',
                     filter = api_filter)

        # Find top voted answers
        for item in answers['items']:
          if not item['question_id'] in answers_hash:
            answers_hash[item['question_id']] = [item['answer_id'], item['score']]

        # Print information
        for question_id, info in answers_hash.items():
          bot.reply_to(message, f"The top voted answer for {question_id} is {info[0]} with a score of {info[1]}")
    except Exception as e:
        bot.reply_to(message, ids)

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