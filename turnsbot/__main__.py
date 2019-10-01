import logging
import os

from turnsbot.utils import Switch, BotAppUpdater, ProdConfig
from turnsbot.turns_bot_app import TurnsBotApp

logger = logging.getLogger('turnsbot.app')
run = Switch()


@run.case('prod')
def run_prod(updater: BotAppUpdater) -> None:
    port = int(os.getenv('PORT', '8443'))
    heroku_app_name = os.environ['HEROKU_APP_NAME']
    config = ProdConfig(port, heroku_app_name)
    updater.run_prod(config)


@run.case('dev')
def run_dev(updater: BotAppUpdater):
    updater.run_dev()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    mode = os.environ['MODE']
    token = os.environ['TOKEN']
    db_uri = os.environ['DB_URI']

    app = TurnsBotApp(logger)
    updater = BotAppUpdater(token, logger)
    updater.mount(app)
    run(mode, updater)
