#!/usr/bin/python3
class Node:
    """
    Definition of class Node for a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance
        Parameters:
        - data (int): The data value of the node.
        - next_node (Node): The next node in the singly linked list.
            Defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node
        Returns:
        - int: The data value of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node

        Args:
            value (int): The new data value

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list
        Returns:
        - Node or None: The next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list
        Parameters:
        - value (Node or None): The new next node
        Raises:
        - TypeError: If value is not a Node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class definition
    """

    def __init__(self):
        """
        Initializes a singly linked list instance with an empty list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Method that inserts a new Node into the correct position
        in the list (increasing order)

        Args:
            value (int): The value of the new node
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list
        Returns:
        - str: A string representation of the linked list
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
