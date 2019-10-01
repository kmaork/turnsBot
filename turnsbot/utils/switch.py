from typing import Callable, Any
from dataclasses import dataclass


@dataclass
class NoSuchCaseException(Exception):
    switch: 'Switch'
    case: Any

    def __str__(self):
        return f'No such case "{self.case}"! Options are: {self.handler.cases.keys()}'


class Switch:
    def __init__(self):
        self.cases = {}

    def add_case(self, case: Any, func: Callable) -> None:
        self.cases[case] = func

    def case(self, case: Any) -> Callable[[Callable], Callable]:
        def decorator(func: Callable) -> Callable:
            self.add_case(case, func)
            return func

        return decorator

    def __call__(self, case: Any, *args: Any, **kwargs: Any) -> Any:
        try:
            handler = self.cases[case]
        except KeyError as e:
            raise NoSuchCaseException(self, case)
        return handler(*args, **kwargs)
