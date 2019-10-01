import logging
import os
from dataclasses import dataclass
from telegram.ext import Updater, CommandHandler
from base64 import urlsafe_b64encode

from .bot_app import BotApp


@dataclass
class ProdConfig:
    port: int
    heroku_app_name: str


@dataclass
class BotAppUpdater:
    def __init__(self, token: str, logger: logging.Logger):
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.logger = logger

    def mount(self, app: BotApp):
        for command, handler in app.handlers:
            self.updater.dispatcher.add_handler(CommandHandler(command, handler))

    def run_dev(self):
        self.logger.info("Starting bot in dev mode")
        self.updater.start_polling()

    def run_prod(self, config: ProdConfig):
        self.logger.info("Starting bot in prod mode")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        self.updater.start_webhook(listen="0.0.0.0",
                                   port=config.port,
                                   url_path=urlsafe_b64encode(os.urandom(10)))
        self.updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(config.heroku_app_name, self.token))
        self.updater.idle()
