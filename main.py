import TelegramChecker
import settings
import logging


logging.basicConfig(filename="bot.log", level=logging.INFO)


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': 
        {
            'username': settings.PROXY_USERNAME, 
            'password': settings.PROXY_PASSWORD
        }
}


if __name__ == "__main__":
    telegram_bot = TelegramChecker.TelegramChecker()
    telegram_bot.run()
