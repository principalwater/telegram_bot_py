# telegram_bot_py
Crunching the telegram bot interface

This project is a Python script that utilizes the Telegram bot API, Dialogflow API, and StackAPI library to build a chatbot that can provide small talk replies, retrieve Stack Overflow answers, and handle natural language text inputs from Telegram users.

To achieve this, the code imports the necessary libraries such as telebot, apiai, json, os, dialogflow, and stackapi. It then sets the Google application credentials and the necessary variables for the Dialogflow API, including the project ID, language code, and session ID. The bot object is initialized using the Telebot library and the necessary command and text message handlers are defined using the message_handler decorator.

The ```start``` command handler replies to users who initiate a conversation with the bot, while the stack command handler retrieves the top voted answers for Stack Overflow questions using the StackAPI library. The text message handler handles all other text inputs by sending them to Dialogflow to be analyzed for intent and returns the corresponding response.

Finally, the code runs the bot using the infinity_polling() function, which continuously polls the Telegram servers for new messages and invokes the corresponding handlers.

It's worth mentioning that this project was run on a remote Linux server as a Linux service, which allowed it to run continuously without the need for manual intervention. This made it easy to deploy and manage the chatbot, even when the local computer was not available.
