#!/usr/bin/python3

"""class node that defines a node"""


class Node:
    """difine node"""

    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        modify value
        raise errors if value is not int or less than 0
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """validate value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """initialize next_node and data"""
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """head of linked list"""
        self.head = None

    def sorted_insert(self, value):
        """insert a new node in a specified position"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        if value < current.data:
            new_node.next_node = current
            self.head = new_node
            return

        while current.next_node is not None and
        current.next_node.data <= value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """prints the linked list"""
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)
