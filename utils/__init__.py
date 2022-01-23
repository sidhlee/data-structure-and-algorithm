from termios import CBAUDEX
from typing import Any, Callable
from time import time


def time_func(cb: Callable[[], Any]):
    start_time = time()
    return_value = cb()
    finish_time = time()
    delta = finish_time - start_time
    return (delta, return_value)
