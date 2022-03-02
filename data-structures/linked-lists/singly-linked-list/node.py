# to postpone the evaluation of annotations: https://stackoverflow.com/a/33533514
# without it, cannot use Node type inside the class declaration
from __future__ import annotations
from typing import Any, Union


class Node:
    next: Union[None, Node]

    def __init__(self, value: Any):
        self.value = value
        self.next = None
