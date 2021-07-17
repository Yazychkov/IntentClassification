from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from source.skillserver import Skillserver
import os


class TelegramChecker:
    def __init__(self):
        self.updater = Updater('KEY', use_context=True)
        self.dp = self.updater.dispatcher
        self.serverskill = Skillserver()

    def run(self):
        logging.info("START")
        self.dp.add_handler(CommandHandler("start", self.start_command))
        self.dp.add_handler(MessageHandler(Filters.text, self.process))
        self.updater.start_polling()
        self.updater.idle()

    def start_command(self, update, context):
        print("start")
        name = update.message.chat.first_name
        update.message.reply_text(f"Привет, {name} 😊!")

    def process(self, update, context):
        text = update.message.text
        try:
            answer = self.serverskill.get_answer(text)
            update.message.reply_text(answer)
        except:
            update.message.reply_text(
                "Причина {}".format(self.serverskill.get_answer(text))
            )

if __name__ == "__main__":
    telegram_bot = TelegramChecker()
    telegram_bot.run()