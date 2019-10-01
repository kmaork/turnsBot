import random
from dataclasses import dataclass
from logging import Logger
from telegram import Update
from telegram.ext import CallbackContext

from .utils import BotApp, handler


@dataclass
class TurnsBotApp(BotApp):
    logger: Logger

    @handler('start')
    def start_handler(self, update: Update, context: CallbackContext):
        # Creating a handler-function for /start command
        self.logger.info("User {} started bot".format(update.effective_user["id"]))
        update.message.reply_text("Hello from Python!\nPress /random to get random number")

    @handler('random')
    def random_handler(self, update: Update, context: CallbackContext):
        # Creating a handler-function for /random command
        print(update.effective_user)
        number = random.randint(0, 10)
        self.logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
        update.message.reply_text("Random number: {}".format(number))
