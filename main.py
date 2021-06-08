import logging
from telegram import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

class TelegramChecker:  
    def __init__(self):
        self.updater = Updater(settings.API_KEY, use_context= True, request_kwargs= PROXY)
        self.dp = self.updater.dispatcher
   
   
    def run(self):
        logging.info('START')
        self.dp.add_handler(CommandHandler("start", self.start_command))
        self.dp.add_handler(MessageHandler(Filters.text, self.process))
        self.updater.start_polling()
        self.updater.idle()


    def start_command(self,update,context):
        print("start")
        name = update.message.chat.first_name
        update.message.reply_text(f'Привет, {name} 😊!')
    
    
    def process(self,update, context):
        text= update.message.text
        update.message.reply_text(text)

if __name__ == "__main__":
    telegram_bot = TelegramChecker()
    telegram_bot.run()
