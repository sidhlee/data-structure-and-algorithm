from abc import ABC, abstractmethod
from typing import Any, TypeVar, Union
from node import Node

T = TypeVar("T")


class BaseLinkedList(ABC):
    length: int
    head: Union[Node, None]
    tail: Union[Node, None]

    @property
    @abstractmethod
    def length(self):
        """The number of nodes in the linked list."""
        pass

    @property
    @abstractmethod
    def head(self):
        """The first node in the linked list."""
        pass

    @property
    @abstractmethod
    def tail(self):
        """The last node in the linked list."""
        pass

    @abstractmethod
    def push(self: T, value: Any) -> T:
        """Creates and inserts a node at the end"""
        pass

    @abstractmethod
    def pop(self) -> Any:
        """Removes the tail node and returns its value"""
        pass

    @abstractmethod
    def shift(self) -> Any:
        """Removes the head node and returns its value"""
        pass

    @abstractmethod
    def unshift(self: T, value: Any) -> T:
        """Creates and inserts a node at the beginning of the list."""

    @abstractmethod
    def get(self, index: int) -> Any:
        """Find a node by its index and return its value."""
        pass

    @abstractmethod
    def set(self: T, value: Any, index: int) -> T:
        """Updates a node value at the given index."""
        pass

    @abstractmethod
    def insert(self: T, value: Any, index: int) -> T:
        """Creates and insert a node at the given index."""
        pass

    @abstractmethod
    def remove(self, index: int) -> Any:
        """Deletes a node at the given index and return its value."""
        pass

    @abstractmethod
    def reverse(self: T) -> T:
        """Reverses the list in place and returns the reversed list."""
        pass


class SinglyLinkedList(BaseLinkedList):
    pass
