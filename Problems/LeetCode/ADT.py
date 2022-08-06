# ERROR classes to be used later
# EMPTY ERROR CLASS
class Empty(Exception):
    """
    To be raised when the list is empty and user want to access it
    """

    pass


# NONETYPE ERROR CLASS
class NoneType(Exception):
    """
    To be raised when the user wants to access a node that is not in the list
    """

    pass


# NODE CLASS
class Node:
    """
    A lightweighted node class to be used for other ADT's.
    """

    def __init__(self, data, next=None, prev=None):
        """
        Initialize a node with data and next/prev pointers.

        Parameters:
        -----------
        data: Any
            The data to be stored in the node.
        next: Node optional
            The next node in the list.
        prev: Node optional
            The previous node in the list.

        Returns:
        --------
        None
        """
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.data)


# SINGLY LINKEDLIST CLASS
class LinkedList:
    """
    A simple implementation of a singly linked list.
    """

    def __init__(self) -> None:
        """
        Initialize a linked list with a head node.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        self.head = None
        self._length = 0

    # @property
    def data(self):
        return self.head.data if self.head is not None else None

    # @property
    def next(self):
        return self.head.next if self.head is not None else None

    def __len__(self) -> int:
        return self._length

    def is_empty(self):
        return self._length == 0

    def list_to_linkedlist(self, list_):
        """
        Converts a list to a linked list.

        Parameters:
        -----------
        list_: List
            The list to be converted.

        Returns:
        --------
        None
        """
        # Check if the list is empty
        if len(list_) == 0:
            raise Empty("The list is empty.")
        # Set the head to the first element of the list
        self.head = Node(list_[0])
        # Set the current node to the head
        current = self.head
        # Loop through the list
        for i in range(1, len(list_)):
            # Create a new node
            new_node = Node(list_[i])
            # Set the current node's next to the new node
            current.next = new_node
            # Set the current node to the new node
            current = new_node
        # Increment the length
        self._length += len(list_)
        # return self.head

    def print_list(self):
        """
        Prints the linked list.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        # Set the current node to the head
        current = self.head
        # Loop until the current node's next is None ie the end of the list
        while current is not None:
            # Print the current node's data
            print(current.data)
            # Set the current node to the current node's next
            current = current.next

    def push(self, data):
        """
        Pushes a node to the beginning of the linked list

        Parameters:
        -----------
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Create a new node
        new_node = Node(data)
        # Set the new node's next to the current head
        new_node.next = self.head
        # Set the head to the new node
        self.head = new_node
        # Increment the length
        self._length += 1

    def insert_after(self, prev_node, data):
        """
        Insert a new node after the given node.

        Parameters:
        -----------
        prev_node: Node
            The node before the new node.
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Check if the given node is not None
        if prev_node is None:
            raise NoneType("The given node is None.")
        # Create a new node
        new_node = Node(data)
        # Set the new_node's next to the prev_node's next
        new_node.next = prev_node.next
        # Set the prev_node's next to the new node
        prev_node.next = new_node
        # Increment the length
        self._length += 1

    def append(self, data):
        """
        Appends a new node to the end of the linked list

        Parameters:
        -----------
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Create a new node
        new_node = Node(data)
        # Check if the head is None
        if self.head is None:
            # Set the head to the new node
            self.head = new_node
        else:
            # Set the current node to the head
            current = self.head
            # Loop until the current node's next is None ie the end of the list
            while current.next is not None:
                # Set the current node to the current node's next
                current = current.next
            # Set the current node's next to the new node
            current.next = new_node
        # Increment the length
        self._length += 1

    def pop(self):
        """
        Removes the last node from the linked list.

        Parameters:
        -----------
        None

        Returns:
        --------
        Any
            The data of the removed node.
        """
        # Check if the head is None
        if self.head is None:
            raise Empty("The linked list is empty.")
        # Set the current node to the head
        current = self.head
        # Loop until the current node's next is None ie the end of the list
        while current.next is not None:
            # Set the current node to the current node's next
            current = current.next
        # Set the previous node's next to None
        current.next = None
        # Decrement the length
        self._length -= 1
        # Return the current node's data
        return current.data

    def remove(self, data):
        """
        Removes the first node with the given data from the linked list.

        Parameters:
        -----------
        data: Any
            The data to be removed.

        Returns:
        --------
        None
        """
        # Check if the head is None
        if self.head is None:
            raise Empty("The linked list is empty.")
        # Set the current node to the head
        current = self.head
        # Check if the current node's (head's) data is the same as the given data
        if current.data == data:
            # Set the head to the head's next
            self.head = current.next
        else:
            # Loop until the current node's next is None ie the end of the list
            while current.next is not None:
                # Check if the current node's next's data is the same as the given data
                if current.next.data == data:
                    # Set the current node's next to the current node's next's next
                    current.next = current.next.next
                    # Decrement the length
                    self._length -= 1
                    # Break the loop
                    break
                # Set the current node to the current node's next
                current = current.next
        # To be executed when the given data is not in the list
        if current.next is None:
            raise NoneType("The given data is not in the list.")


class DoublyLinkedList:
    """
    A simple implementation of the doubly linked list
    """

    def __init__(self):
        self.head = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def push(self, data):
        """
        Pushes a node to the beginning of the DLL

        Parameters:
        -----------
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Create a new node
        new_node = Node(data)
        # Set the new node's next to the current head
        new_node.next = self.head
        # check if the head is not None
        if self.head is not None:
            # Set the head's prev to the new node
            self.head.prev = new_node
        # Set the head to the new node
        self.head = new_node
        # Increment the length
        self._length += 1

    def insert_after(self, prev_node, data):
        """
        Inserts a new node after the given previous node.

        Parameters:
        -----------
        prev: Node
            The node before the new node.
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Check if the given node is not None
        if prev_node is None:
            raise NoneType("The given node is None.")
        # Create a new node
        new_node = Node(data)
        # Set the new_node's next to the prev_node's next
        new_node.next = prev_node.next
        # Set the prev_node's next to the new node
        prev_node.next = new_node
        # Set the new_node's prev to the prev_node
        new_node.prev = prev_node
        # Check if the new_node's next is not None
        if new_node.next is not None:
            # Set the new_node's next's prev to the new node
            new_node.next.prev = new_node
        # Increment the length
        self._length += 1

    def insert_before(self, next_node, data):
        """
        Inserts a node before the given node.

        Parameters:
        -----------
        next_node: Node
            The node after the new node.
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Check if the given node is not None
        if next_node is None:
            raise NoneType("The given node is None.")
        # Create a new node
        new_node = Node(data)
        # Set the next of the new node to the next_node
        new_node.next = next_node
        # Set the new_node's prev to the next_node's prev
        new_node.prev = next_node.prev
        # Check if the next_node's prev is None
        if next_node.prev is None:
            # Set the head to the new node
            self.head = new_node
        else:
            # Set the new_node's prev's next to the new node
            new_node.prev.next = new_node
        # set the prev of the next_node to the new node
        next_node.prev = new_node
        # Increment the length
        self._length += 1

    def append(self, data):
        """
        Appends a new node to the end of the DLL

        Parameters:
        -----------
        data: Any
            The data to be stored in the node.

        Returns:
        --------
        None
        """
        # Create a new node
        new_node = Node(data)
        # Check if the head is None
        if self.head is None:
            # Set the head to the new node
            self.head = new_node
        else:
            # Set the current node to the head
            current = self.head
            # Loop until the current node's next is None ie the end of the list
            while current.next is not None:
                # Set the current node to the current node's next
                current = current.next
            # Set the current node's next to the new node
            current.next = new_node
            # Set the new_node's prev to the current node
            new_node.prev = current
        # Increment the length
        self._length += 1

    def print_list(self):
        """
        Prints the linked list.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        # Check if the head is None
        if self.head is None:
            raise Empty("The linked list is empty.")
        # Set the current node to the head
        current = self.head
        # Loop until the current node's next is None ie the end of the list
        while current is not None:
            # Print the current node's data
            print(current.data)
            # Set the current node to the current node's next
            current = current.next

    def pop(self):
        """
        Removes the last node from the DLL.

        Parameters:
        -----------
        None

        Returns:
        --------
        data: Any
            The data of the removed node.
        """
        # Check if the head is None
        if self.head is None:
            raise Empty("The linked list is empty.")
        # Set the current node to the head
        current = self.head
        # Loop until the current node's next is None ie the end of the list
        while current.next is not None:
            # Set the current node to the current node's next
            current = current.next
        # Set the current node's prev's next to None
        print(current)
        if current.prev is not None:
            current.prev.next = None
        else:
            self.head = None
        # Get the data
        data = current.data
        # Decrement the length
        self._length -= 1
        # Return the data
        return data
