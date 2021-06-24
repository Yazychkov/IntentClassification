import telegram_connector
import logging


logging.basicConfig(filename="bot.log", level=logging.INFO)



if __name__ == "__main__":
    telegram_bot = telegram_connector.TelegramChecker()
    telegram_bot.run()
