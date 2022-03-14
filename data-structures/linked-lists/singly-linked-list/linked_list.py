from abc import ABC, abstractmethod
from typing import Any, TypeVar, Union
from node import Node

T = TypeVar("T")


class BaseLinkedList(ABC):
    length: int
    head: Union[Node, None]
    tail: Union[Node, None]

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        super().__init__()

    # @property
    # @abstractmethod
    # def length(self):
    #     """The number of nodes in the linked list."""
    #     pass

    # @property
    # @abstractmethod
    # def head(self):
    #     """The first node in the linked list."""
    #     pass

    # @property
    # @abstractmethod
    # def tail(self):
    #     """The last node in the linked list."""
    #     pass

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
    def __init__(self):
        super().__init__()

    def push(self, value):
        node = Node(value)
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self

    def pop(self):

        if self.head is not None:
            popped_value = self.tail.value
            current_node = self.head
            current_node_temp = None

            def is_tail(node: Node):
                return node.next is None

            while not is_tail(current_node):
                current_node_temp = current_node
                current_node = current_node.next
            # current_node is now the one before the tail
            self.tail = current_node_temp
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return popped_value
        else:
            return None

    def unshift(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node

        return self

    def shift(self):
        if self.length == 0:
            return None
        shifted = self.head
        self.head = shifted.next
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return shifted.value

    def get(self, index: int):
        if index >= self.length or not self.head or not self.tail:
            raise IndexError
        if index == self.length - 1:
            return self.tail.value
        current_index = 0
        current_node = self.head
        while current_index < index and current_node.next is not None:
            current_index += 1
            current_node = current_node.next
        return current_node.value

    def set(self, value, index):
        if index >= self.length or not self.head or not self.tail:
            raise IndexError
        if index == 0:
            self.head.value = value
        elif index == self.length - 1:
            self.tail.value = value
        else:
            current_index = 0
            current_node = self.head
            while current_node.next is not None and current_index < index:
                current_index += 1
                current_node = current_node.next
            current_node.value = value

        return self

    def insert(self, value: Any, inserting_index: int):
        if not (0 <= inserting_index <= self.length):
            raise IndexError
        inserting_node = Node(value)

        if inserting_index == 0:
            return self.unshift(value)

        # Inserting after tail
        if inserting_index == self.length:
            return self.push(value)

        # all other cases: 0 < inserting_index <= self.length
        current_node = self.head
        # python-way of non-null assertion
        assert current_node is not None
        current_index = 0
        while current_index < self.length and current_node.next is not None:
            if current_index == inserting_index - 1:
                prev_node = current_node
                next_node = current_node.next
                prev_node.next = inserting_node
                inserting_node.next = next_node
                self.length += 1
                return self
            current_node = current_node.next
            current_index += 1

    def remove(self):
        ...

    def reverse(self):
        ...
