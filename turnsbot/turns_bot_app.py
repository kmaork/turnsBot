import random
from dataclasses import dataclass
from logging import Logger
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from .utils import BotApp, command_handler


@dataclass
class TurnsBotApp(BotApp):
    logger: Logger

    @command_handler('start')
    def start_handler(self, update: Update, context: CallbackContext):
        chat_id = update.effective_user['id']
        self.logger.info(f'User {chat_id} started bot')
        keyboard = [[InlineKeyboardButton('Adooba!', callback_data='blob'),
                     InlineKeyboardButton('Berem berem!', callback_data='blob')]]
        markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_html(text='Text:', reply_markup=markup)

    def __reply_keyboard(self, update: Update, context: CallbackContext):
        keyboard = [['Dooda li doo', 'Bingabong']]
        markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_html(text='Text:', reply_markup=markup)

    @command_handler('random')
    def random_handler(self, update: Update, context: CallbackContext):
        number = random.randint(0, 10)
        self.logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
        update.message.reply_text("Random number: {}".format(number))
