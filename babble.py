#!/usr/bin/env python3

from config import TELEGRAM_BOT_TOKEN as token
from user import User
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.command | Filters.text,
                                          handler, pass_user_data=True))
    updater.start_polling()

def handler(bot, update, user_data):
    if 0 not in user_data:
        user_data[0] = User()
    bot.send_message(chat_id=update.message.chat_id,
                     text=user_data[0].handle(update.message.text))

if __name__ == '__main__':
    main()
