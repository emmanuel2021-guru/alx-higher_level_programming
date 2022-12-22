#!/usr/bin/python3

"""Define a Node"""


class Node:
    """Represents a Node"""
    def __init__(self, data, next_node=None):
        """Initializes a Node instance
           and checks for exceptions

           Args:
            data (int): the data stored
                        in the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for retrieving
           the data stored in the Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for storing
           the data in the Node
        """
        try:
            if type(value) is not int:
                raise TypeError
            else:
                self.__data = value
        except TypeError:
            print("data must be an integer")
    
    @property
    def next_node(self):
        """Getter method for retrieving
           the next Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for creating
           the next Node
        """
        try:
            if type(value) is not Node and value != None:
                raise TypeError
            else:
                self.__next_node = value
        except TypeError:
            print("next_node must be a Node object")


"""Define a singly linked list"""


class SinglyLinkedList:
    """Represents a singly linked list"""
    self.__head = None
    def __init__(self):
        """Initializes a singly linked list"""
    

    def sorted_insert(self, value):
        """Inserts a new Node into the correct
           sorted position in the list
           (increasing order)
        """
        if self.__head == None:
            self.__head = Node()
            self.__head.data(value)
        else:
            self.__head.data(value)
