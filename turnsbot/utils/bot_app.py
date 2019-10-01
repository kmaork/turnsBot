from functools import partial
from typing import Callable, Type, Dict, Tuple, List


class BotAppMeta(type):
    def __new__(mcs, what, bases, dict):
        return super().__new__(mcs, what, bases, {**dict, 'COMMAND_HANDLERS': {}})


class BotApp(metaclass=BotAppMeta):
    COMMAND_HANDLERS: Dict[str, Callable]

    @property
    def command_handlers(self) -> List[Tuple[str, Callable]]:
        handlers = []
        for command, handler in self.COMMAND_HANDLERS.items():
            handlers.append((command, partial(handler, self)))
        return handlers

    @classmethod
    def add_command_handler(cls, command: str, handler: Callable):
        cls.COMMAND_HANDLERS[command] = handler


class command_handler:
    def __init__(self, command: str):
        self.command = command

    def __call__(self, func: Callable):
        self.func = func
        return self

    def __set_name__(self, owner: Type[BotApp], name):
        owner.add_command_handler(self.command, self.func)
