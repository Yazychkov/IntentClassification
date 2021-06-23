from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
from skillserver import Skillserver


class TelegramChecker:
    def __init__(self):
        self.updater = Updater(settings.API_KEY, use_context=True)
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
                "Технические неполадки, пожалуйста, попробуйте позднее."
            )
