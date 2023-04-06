# telegram_bot_py
Crunching the telegram bot interface

This project is a Python script that utilizes the Telegram bot API, Dialogflow API, and StackAPI library to build a chatbot that can provide small talk replies, retrieve Stack Overflow answers, and handle natural language text inputs from Telegram users. The bot interacts with users by sending and receiving messages in natural language. The apiai and dialogflow libraries are used to process user messages and generate responses using machine learning algorithms.

To achieve this, the code imports the necessary libraries. It then sets the Google application credentials and the necessary variables for the ```Dialogflow API```, including the project ID, language code, and session ID. The bot object is initialized using the Telebot library and the necessary command and text message handlers are defined using the ```message_handler``` decorator.

The bot is also integrated with StackOverflow through the ```stackapi``` library. When a user sends the ```/stack``` command followed by a question ID, the bot queries the StackOverflow API to find the top voted answer for that question ID. The bot then sends a message to the user with the answer ID and the score of that answer.

The os library is used to set the Google Application Credentials needed for the dialogflow library to access the chatbot's Dialogflow agent. The ```google.api_core.exceptions``` library is used to handle exceptions that may occur when connecting to the Dialogflow agent.

The script includes message handlers that respond to user input. The ```send_start()``` function sends a welcome message when a user starts a chat session with the bot. The ```send_msg()``` function processes any text messages sent by the user and uses Dialogflow to generate a response. The ```stack_find()``` function processes the ```/stack``` command and sends a message to the user with the top voted answer for the specified question ID.

Finally, the ```bot.infinity_polling()``` method is used to start the bot and allow it to run indefinitely, waiting for new messages from users.

It's worth mentioning that this project was run on a remote Linux server as a Linux service, which allowed it to run continuously without the need for manual intervention. This made it easy to deploy and manage the chatbot, even when the local computer was not available.
