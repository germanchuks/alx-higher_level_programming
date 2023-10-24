#!/usr/bin/python3
"""Define class for a Singly-linked List."""


class Node:
    """
    Represent a node in a singly-linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Args:
            data (int): The data of the new node.
            next_node (Node): The next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data of the node.

        Returns:
            int: The node data.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for the data of the node.

        Args:
            value (int): Data of the node. It must be a integer value.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next node.

        Returns:
            int: The next node.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next node.

        Args:
            value (int): The next node. Can be None or must be a Node .

        Raises:
            TypeError: If the provided value is not a Node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly_linked list.
    """

    def __init__(self):
        """
        Initializes a new singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position (increasing order)
        in the singly linked list.

        Args:
            value (Node): The new node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                   current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        Defines the print() representation of the singly linked list.
        """
        values = []
        current_node = self.__head
        while current_node is not None:
            values.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(values))
