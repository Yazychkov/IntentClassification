from source.telegram_connector import TelegramChecker
import logging


logging.basicConfig(filename="bot.log", level=logging.INFO)



if __name__ == "__main__":
    telegram_bot = TelegramChecker()
    telegram_bot.run()
