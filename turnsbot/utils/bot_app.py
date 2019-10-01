from functools import partial
from typing import Callable, Type, Dict, Tuple, List


class BotAppMeta(type):
    def __new__(mcs, what, bases, dict):
        return super().__new__(mcs, what, bases, {**dict, 'HANDLERS': {}})


class BotApp(metaclass=BotAppMeta):
    HANDLERS: Dict[str, Callable]

    @property
    def handlers(self) -> List[Tuple[str, Callable]]:
        handlers = []
        for command, handler in self.HANDLERS.items():
            handlers.append((command, partial(handler, self)))
        return handlers

    @classmethod
    def add_handler(cls, command: str, handler: Callable):
        cls.HANDLERS[command] = handler


class handler:
    def __init__(self, command: str):
        self.command = command

    def __call__(self, func: Callable):
        self.func = func
        return self

    def __set_name__(self, owner: Type[BotApp], name):
        owner.add_handler(self.command, self.func)
