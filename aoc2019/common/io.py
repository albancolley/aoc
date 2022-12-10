import logging
from typing import Callable, Any


def load_file(filename: str, handler: Callable[[[str]], Any] = None) -> [str]:
    file = open(filename, "r")
    data = file.read().splitlines()
    if handler:
        data = handler(data)

    return data
